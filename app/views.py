import json
import logging
import os
import shutil
from datetime import datetime
from zipfile import ZipFile

import boto3
import psycopg2
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.db import IntegrityError
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect
from django.shortcuts import render
from django.template.loader import render_to_string
from django.urls import reverse
from django.urls import reverse_lazy
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode

from . import utils
from .forms import MetadataForm
from .models import Metadata, Results, Status, User

# Create your views here.
logger = logging.getLogger('django')


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'password_reset.html'
    email_template_name = 'email_template_password_reset.html'
    subject_template_name = 'password_reset_subject'
    success_url = reverse_lazy('password_reset_sent_email')


class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return str(user.is_active) + str(user.pk) + str(timestamp)


account_activation_token = TokenGenerator()



def home(request):
    if request.method == "POST":
        form = MetadataForm(request.POST)
        if form.is_valid():
            return redirect("table")
    else:
        form = MetadataForm()
    return render(request, "home.html", {"form": form})


def featuretable(request):
    return render(request, "featuretable.html")


# class ExampleView(TemplateView):
#     template_name = 'app/templates/home.html'

#     def get_template_names(self):
#         if 'template' in self.request.GET:
#             template_name = self.request.GET['template']
#             return [f'../../app/static/visualiazation/{template_name}.html']
#         else:
#             return [self.template_name]

# def taxonomy_overview(request,uuid):
#     return render(request, "visualization/"+uuid+"/data/index.html")

# def featuretable_overview(request,uuid):
#     # s3 = boto3.client('s3')
#     # bucket_name = 'qiime2storage'
#     # object_key = 'merged_results/'+uuid+'/merged_feature_tables/data/index.html'
#     # response = s3.get_object(Bucket=bucket_name, Key=object_key)
#     # html_content = response['Body'].read().decode('utf-8')
#     # return HttpResponse(html_content)
#     return render(request, "visualization/"+uuid+"/data/index.html")

# def featuretable_interactive(request,uuid):
#     # create an S3 client
#     s3 = boto3.client('s3')

#     # specify the S3 bucket and file names
#     bucket_name = 'qiime2storage'
#     html_file = 'merged_results/'+uuid+'/merged_feature_tables/data/index.html'
#     css_file = 'merged_results/'+uuid+'/merged_feature_tables/data/q2templateassets/css/bootstrap.min.css'


#     # download the files from S3 and store them temporarily on the server
#     s3.download_file(bucket_name, html_file, '/visualization/index.html')
#     s3.download_file(bucket_name, css_file, '/visualization/bootstrap.min.css')


#     # define a context dictionary with any variables you want to pass to the template
#     context = {

#     }

#     # render the HTML template with the context dictionary
#     return render(request, '/visualization/index.html', context)

# API end point to get run status by run ID (/api/check_run_status/{runId})
def check_run_status(request, runId):
    conn = psycopg2.connect(
        database=os.environ.get('DB_NAME'),
        user=os.environ.get('DB_USER'),
        password=os.environ.get('DB_PASSWORD'),
        host=os.environ.get('DB_HOST'),
        port=os.environ.get('DB_PORT')
    )

    cur = conn.cursor()
    cur.execute("SELECT * FROM status where acc = %s", (runId,))
    row = cur.fetchone()

    if not row:
        if request.user.is_authenticated:
            cur.execute(f"""INSERT INTO status (acc, user_id, email, public, status, created_at, updated_at) 
                                                VALUES ('{runId}', '{request.user.id}', '{request.user.email}', '1', 0, 
                                                NOW(), NOW())""")
        else:
            cur.execute(f"""INSERT INTO status (acc, public, status, created_at, updated_at) VALUES ('{runId}', '1', 0, NOW(), NOW())""")

        conn.commit()
        cur.execute("SELECT * FROM status where acc = %s", (runId,))
        row = cur.fetchone()

    columns = [desc[0] for desc in cur.description]
    row_dict = dict(zip(columns, row))
    # Convert any datetime objects to strings
    for key, value in row_dict.items():
        if isinstance(value, datetime):
            row_dict[key] = value.strftime("%m/%d/%Y")
    json_data = json.dumps(row_dict)

    cur.close()
    conn.close()

    return HttpResponse(json_data, content_type='application/json')


def demo_table_view(request):
    return render(request, "demo_table_view.html")


def unzip(zip_file_path, output_dir):
    with ZipFile(zip_file_path, 'r') as z:
        z.extractall(path=output_dir)


def move_data_folder(output_dir, folder_name):
    done = False
    for root, sub_dirs, file_names in os.walk(output_dir):
        if done:
            break
        for sub_dir in sub_dirs:
            if sub_dir == 'data':
                shutil.move(os.path.join(root, sub_dir), os.path.join(output_dir, folder_name))
                done = True
                break


def feature_table_summary(request, uuid):
    # uuid = request.GET.get('uuid', None)
    if uuid is not None and "demo" not in uuid:
        # Option 1) use shell command to copy files from s3 bucket to /app/static/visualization/
        # shutil.copytree('/home/qiime2/qiime2storage/merged_results/'+uuid+'/feature_table/','app/static/visualization/'+uuid+'/feature_table/')

        # Option 2) use boto3 to download files from s3 bucket
        # create an S3 client
        s3 = boto3.client('s3')

        # specify the S3 bucket and file names
        bucket_name = 'qiime2storage'
        qzv_file = 'merged_results/' + uuid + '/merged_feature_tables.qzv'

        # download the files from S3 and store them temporarily on the server
        target_folder = os.path.join(settings.BASE_DIR, 'app', 'static', 'visualization', uuid)
        if not os.path.exists(target_folder):
            os.makedirs(target_folder)
        s3.download_file(bucket_name, qzv_file, target_folder + "/merged_feature_tables.qzv")
        # unzip qzv file
        unzip(target_folder + "/merged_feature_tables.qzv", target_folder)

        # re-organize the folder
        move_data_folder(target_folder, 'feature_table')

        return render(request, "feature_table_summary.html", {"chart_type": "live", "uuid": uuid})
    else:
        # show demo chart
        return render(request, "feature_table_summary.html", {"chart_type": "demo", "uuid": "demo"})


def taxonomic_bar_plots(request, uuid):
    # uuid = request.GET.get('uuid', None)
    if uuid is not None and "demo" not in uuid:
        # Option 1) use shell command to copy files from s3 bucket to /app/static/visualization/
        # shutil.copytree('/home/qiime2/qiime2storage/merged_results/'+uuid+'/taxonomy_results/','app/static/visualization/'+uuid+'/taxonomy_results/')

        # Option 2) use boto3 to download files from s3 bucket
        # create an S3 client
        s3 = boto3.client('s3')

        # specify the S3 bucket and file names
        bucket_name = 'qiime2storage'
        qzv_file = 'merged_results/' + uuid + '/taxonomy_bar_plot.qzv'

        # download the files from S3 and store them temporarily on the server
        target_folder = os.path.join(settings.BASE_DIR, 'app', 'static', 'visualization', uuid)
        if not os.path.exists(target_folder):
            os.makedirs(target_folder)
        s3.download_file(bucket_name, qzv_file, target_folder + "/taxonomy_bar_plot.qzv")
        # unzip qzv file
        unzip(target_folder + "/taxonomy_bar_plot.qzv", target_folder)

        # re-organize the folder
        move_data_folder(target_folder, 'taxonomy_results')

        return render(request, "taxonomic_bar_plots.html", {"chart_type": "live", "uuid": uuid})
    else:
        # show demo chart
        return render(request, "taxonomic_bar_plots.html", {"chart_type": "demo", "uuid": "demo"})


def generate_visualization(request):
    if request.method == 'POST':
        # define the pattern for the checkbox names
        pattern = 'chk_'

        runIds = ""
        # loop through the request.POST dictionary to find the names of the checkboxes
        for name, value in request.POST.items():
            if name.startswith(pattern):
                # do something if the checkbox is checked
                runIds = runIds + " " + value
    else:
        # temporarily add runIds
        runIds = "ERR6004724 ERR6004803 ERR6004727 ERR6004692"

    return render(request, "visualization.html", {"runIds": runIds.strip()})


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("home"))
        else:
            return render(request, "login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("home"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        first_name = request.POST["first-name"]
        last_name = request.POST["last-name"]

        # Check if the given email is already registered
        if User.objects.filter(email__iexact=email).count() > 0:
            return render(request, "register.html", {"error_message": [f"{email} is already registered."]})

        # Check if the given username is already registered
        if User.objects.filter(username__iexact=username).count() > 0:
            return render(request, "register.html", {"error_message": [f"{username} is already taken."]})

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "register.html", {"error_message": ["Passwords must match."]})

        # Validate password
        success, msg = utils.validate_password(password)

        if not success:
            return render(request, "register.html", {"error_message": [msg]})

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.first_name = first_name
            user.last_name = last_name
            user.is_active = False
            user.save()
        except IntegrityError:
            return render(request, "register.html", {
                "error_message": ["Username already taken."]
            })
        # login(request, user)
        current_site = get_current_site(request)

        mail_subject = 'Activate your account.'
        message = render_to_string('email_template_verification.html', {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user),
        })

        send_mail(mail_subject, message, 'microbiome.platform@gmail.com', [email], fail_silently=False)

        return render(request, "register.html", {
            "success_message": [f"We sent an email to {email}.", "Please confirm your email address to complete your "
                                                                 "registration."]
        })
    else:
        return render(request, "register.html")


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return render(request, "login.html", {"success_message": f"Your account is activated."})
    else:
        return HttpResponse('Activation link is invalid!')


def password_reset_sent_email(request):
    return render(request, "password_reset_sent_email.html")


@login_required(login_url="login")
def status(request, username, page=1):
    status_list = Status.objects.filter(user_id=username)
    paginator = Paginator(status_list, per_page=16)
    page_object = paginator.page(page)

    return render(request, "status.html", {
        "username": username,
        "statuses": page_object
    })


@login_required(login_url="login")
def history(request, username, page=1):
    metadata_list = Metadata.objects.all()
    paginator = Paginator(metadata_list, per_page=20)
    page_object = paginator.page(page)

    return render(request, "history.html", {
        "username": username,
        "histories": page_object
    })


@login_required(login_url="login")
def delete_account_confirm(request, username):
    return render(request, "delete_account.html", {"username": username})


@login_required(login_url="login")
def delete_account(request, username):
    if request.method == "POST":
        logout(request)
        user = User.objects.get(username=username)
        user.delete()

        return render(request, "register.html", {
            "success_message": [f"Your account has been deleted successfully."]
        })

    else:
        return HttpResponseRedirect(reverse("home"))


@login_required(login_url="login")
def user_profile(request, username, page=1, show_history=0):
    user = User.objects.get(username=username)

    result_list = Results.objects.all();
    paginator = Paginator(result_list, per_page=16)
    page_object = paginator.page(page)

    return render(request, "user_profile.html", {
        "username": username,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "email": user.email,
        "date_joined": user.date_joined.date(),
        "results": page_object,
        "show_history": show_history
    })


@login_required(login_url="login")
def edit_profile(request, field):
    """
    Edit the user and then return the serialized data of the object.
    """
    if request.method == "PUT":
        # Get the form data
        user = User.objects.get(username=request.user.username)
        data = json.loads(request.body)
        updated_content = data.get("content")

        # Update the user
        if field == "firstName":
            if updated_content is not None and updated_content != '':
                user.first_name = data["content"]
            updated_content = user.first_name

        elif field == "lastName":
            if updated_content is not None and updated_content != '':
                user.last_name = data["content"]
            updated_content = user.last_name

        user.save()
        # Return updated_content
        return JsonResponse({"content": updated_content})

    # Edit must be via PUT
    else:
        return JsonResponse({"error": "PUT request required."}, status=400)


@login_required(login_url="login")
def change_password(request):
    if request.method != "PUT":
        # PUT method is required
        return JsonResponse({"error": "PUT request required."}, status=400)

    # Get the form data
    data = json.loads(request.body)

    current_password = data.get("currPwd")
    new_password = data.get("newPwd")
    confirm_new_password = data.get("confNewPwd")

    user = User.objects.get(username=request.user.username)

    # Check current password
    if not user.check_password(current_password):
        return JsonResponse({"success": False, "message": "Current password was not correct."})

    # Check if passwords match
    if new_password != confirm_new_password:
        return JsonResponse({"success": False, "message": "New passwords don't match."})

    # Check if new password is different from current password
    if new_password == current_password:
        return JsonResponse({"success": False, "message": "New password must be different from current password."})

    # Validate password
    success, msg = utils.validate_password(new_password)

    if success:
        user.set_password(new_password)
        user.save()

    # Return new password
    return JsonResponse({"success": success, "message": msg})


def build_query(filter_values, field):
    queries = [Q(**{field: f}) for f in filter_values]

    # Take one Q object from the list
    query = queries.pop()

    # Or the Q object with the ones remaining in the list
    for item in queries:
        query |= item

    return query


def search(request, page=1, order_by='acc', direction='asc'):
    if request.method == 'POST':
        metadata_fields = ['librarylayout', 'sra_study', 'center_name', 'experiment', 'sample_acc', 'biosample',
                           'organism', 'bioproject', 'geo_loc_name_country_calc', 'geo_loc_name_country_continent_calc']

        query_set_metadata = None

        search_criteria = {}

        for metadata_field in metadata_fields:
            filter_values = request.POST.getlist(metadata_field)

            if not filter_values:
                continue

            search_criteria[metadata_field] = filter_values
            query = build_query(filter_values=filter_values, field=metadata_field)

            if query_set_metadata:
                query_set_metadata = query_set_metadata.filter(query)
            else:
                query_set_metadata = Metadata.objects.filter(query)

        num_records = query_set_metadata.count()

        paginator = Paginator(query_set_metadata.order_by(order_by), per_page=20)
        page_object = paginator.page(page)

        query_set_in_progress = Status.objects.filter(status=0).values_list('acc', flat=True) | Status.objects.filter(
            status=1).values_list('acc', flat=True)
        query_set_complete = Status.objects.filter(status=2).values_list('acc', flat=True)
        query_set_error = Status.objects.filter(status=3).values_list('acc', flat=True)

        in_progress_accs = set(list(query_set_in_progress))
        completed_accs = set(list(query_set_complete))
        errored_accs = set(list(query_set_error))

        if request.user.is_authenticated:
            username = request.user.username
        else:
            username = None

        return render(request, 'table.html', {'metadata': page_object,
                                              'in_progress_accs': in_progress_accs,
                                              'completed_accs': completed_accs,
                                              'errored_accs': errored_accs,
                                              'username': username,
                                              'order_by': order_by,
                                              'direction': direction,
                                              'num_records': num_records,
                                              'search_criteria': json.dumps(search_criteria)})
    elif request.method == 'GET':

        if direction == 'desc':
            ordering = '-{}'.format(order_by)
        else:
            ordering = order_by

        query_set_metadata = None
        search_criteria_json = request.GET.get('search_criteria')

        search_criteria = json.loads(search_criteria_json)

        for metadata_field, filter_values in search_criteria.items():
            if not filter_values:
                continue

            query = build_query(filter_values=filter_values, field=metadata_field)

            if query_set_metadata:
                query_set_metadata = query_set_metadata.filter(query)
            else:
                query_set_metadata = Metadata.objects.filter(query)

        paginator = Paginator(query_set_metadata.order_by(ordering), per_page=20)
        page_object = paginator.page(page)

        num_records = query_set_metadata.count()

        query_set_in_progress = Status.objects.filter(status=0).values_list('acc', flat=True) | Status.objects.filter(
            status=1).values_list('acc', flat=True)
        query_set_complete = Status.objects.filter(status=2).values_list('acc', flat=True)
        query_set_error = Status.objects.filter(status=3).values_list('acc', flat=True)

        in_progress_accs = set(list(query_set_in_progress))
        completed_accs = set(list(query_set_complete))
        errored_accs = set(list(query_set_error))

        if request.user.is_authenticated:
            username = request.user.username
        else:
            username = None

        return render(request, 'table.html', {'metadata': page_object,
                                              'in_progress_accs': in_progress_accs,
                                              'completed_accs': completed_accs,
                                              'errored_accs': errored_accs,
                                              'username': username,
                                              'order_by': order_by,
                                              'direction': direction,
                                              'num_records': num_records,
                                              'search_criteria': json.dumps(search_criteria)})








    else:
        return render(request, 'page_not_found.html')