import json
import logging
import os
import shutil
from datetime import datetime
from zipfile import ZipFile
from time import time


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
from .models import Metadata, Results, Status, User, History

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
session_key_visual = 'update_runId_for_visual'


def home(request):
    if request.method == "POST":
        form = MetadataForm(request.POST)
        if form.is_valid():
            return redirect("table")
    else:
        if (request.session.get('save_form', None) != None):
            saved_form = json.loads(request.session.get('save_form', None))
            form = MetadataForm(initial= saved_form )
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

# API end point to reset selected run ID for visualization (api/visualization/reset)
def reset_runId_for_visual(request):
    utils.clear_session_list(request, session_key_visual)
    json_data = json.dumps(request.session.get(session_key_visual, []))
    return HttpResponse(json_data, content_type='application/json')

# API end point to update selected run ID for visualization (api/visualization/{add}/{runId})
def update_runId_for_visual(request, runId, add = 1):
    if isinstance(add, int) and isinstance(runId, str):
        
        utils.update_session_list(request,session_key_visual,runId,add)

    json_data = json.dumps(request.session.get(session_key_visual, []))
    return HttpResponse(json_data, content_type='application/json')


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
            cur.execute("INSERT INTO status (acc, user_id, email, public, status, created_at, updated_at) \
             VALUES (%s, %s, %s, %s, %s, NOW(), NOW())",
            (runId, request.user.id, request.user.email, '1', 0,))
           
        else:
            cur.execute("INSERT INTO status (acc, public, status, created_at, updated_at) \
                                        VALUES (%s, %s, %s, NOW(), NOW())",
                    (runId,'1',0,))

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
    try:
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
    except:
        return render(request, "feature_table_summary.html", {"chart_type": "demo", "uuid": "demo"})

def taxonomic_bar_plots(request, uuid):
    try:
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
    except:
        return render(request, "taxonomic_bar_plots.html", {"chart_type": "demo", "uuid": "demo"})

def generate_visualization(request):
    runIds = ""
    # load selected runIds from session
    sel_runIds_visual = request.session.get(session_key_visual, [])
    if len(sel_runIds_visual) >0:
        for runId in sel_runIds_visual:
            runIds += " " +runId
    
    # if request.method == 'POST':
    #     # define the pattern for the checkbox names
    #     pattern = 'chk_'

    #     runIds = ""
    #     # loop through the request.POST dictionary to find the names of the checkboxes
    #     for name, value in request.POST.items():
    #         if name.startswith(pattern):
    #             # do something if the checkbox is checked
    #             runIds = runIds + " " + value
    # else:
    #     # temporarily add runIds
    #     runIds = "ERR6004724 ERR6004803 ERR6004727 ERR6004692"

    return render(request, "visualization.html", {"runIds": runIds.strip()})


#download result csv file from the S3 bucket
def download_results_csv(request,uuid):
    try:
    # uuid = request.GET.get('uuid', None)
        if uuid is not None and "demo" not in uuid:
            # Option 1) use shell command to copy files from s3 bucket to /app/static/visualization/
            # shutil.copytree('/home/qiime2/qiime2storage/merged_results/'+uuid+'/taxonomy_results/','app/static/visualization/'+uuid+'/taxonomy_results/')

            # Option 2) use boto3 to download files from s3 bucket
            # create an S3 client
            s3 = boto3.client('s3')

            # specify the S3 bucket and file names
            bucket_name = 'qiime2storage'
         
            csv_file = 'merged_results/' + uuid + '/results.csv'

            # download the files from S3 and store them temporarily on the server
            target_folder = os.path.join(settings.BASE_DIR, 'app', 'static', 'visualization', uuid)
            if not os.path.exists(target_folder):
                os.makedirs(target_folder)
           
            s3.download_file(bucket_name, csv_file, target_folder + "/results.csv")

            if not os.path.exists(target_folder + "/results.csv"):
                return HttpResponse("The file does not exist.", status=404)
            
            # Open the file and read the CSV data
            with open(target_folder + "/results.csv", 'r') as f:
                csv_data = f.read()
            
            # Create the HttpResponse object with the CSV data
            response = HttpResponse(csv_data, content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="results.csv"'
            
            return response

            
        else:
            return HttpResponse("The file does not exist.", status=404)
    except:
        return HttpResponse("The file does not exist.", status=404)

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
    search_history_list = History.objects.filter(user_id=username)
    paginator = Paginator(search_history_list, per_page=20)
    page_object = paginator.page(page)

    return render(request, "history.html", {
        "username": username,
        "searches": page_object
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
    t0 = time()
    if request.method == 'POST':
        metadata_fields = ['librarylayout', 'sra_study', 'center_name', 'experiment', 'sample_acc', 'biosample',
                           'organism', 'bioproject', 'geo_loc_name_country_calc', 'geo_loc_name_country_continent_calc',
                           'ecotype_sam', 'cultivar_sam', 'breed_sam', 'strain_sam', 'iosolate_sam', 'race_ethnicity',
                           'gender', 'libraryselection']

        query_set_metadata = None

        search_criteria = {}

        for metadata_field in metadata_fields:
            t_init = time()
            filter_values = request.POST.getlist(metadata_field)
            
            if not filter_values:
                continue


           
            search_criteria[metadata_field] = filter_values
            query = build_query(filter_values=filter_values, field=metadata_field)

            if query_set_metadata:
                query_set_metadata = query_set_metadata.filter(query)
            else:
                query_set_metadata = Metadata.objects.filter(query)

            t_finish = time()
            print(f'Built {metadata_field}: {t_finish - t_init}')

        clean_form = json.dumps(search_criteria,default=str)
        request.session['save_form'] = clean_form

        t1 = time()
        print(f'Built Query sets: {t1 - t0}')

        num_records = query_set_metadata.count()

        t2 = time()
        print(f'num_records: {t2 - t1}')

        paginator = Paginator(query_set_metadata.order_by(order_by), per_page=20)
        page_object = paginator.page(page)

        t3 = time()
        print(f'pagination: {t3 - t2}')

        query_set_in_progress = Status.objects.filter(status=0).values_list('acc', flat=True) | Status.objects.filter(
            status=1).values_list('acc', flat=True)
        query_set_complete = Status.objects.filter(status=2).values_list('acc', flat=True)
        query_set_error = Status.objects.filter(status=3).values_list('acc', flat=True)

        t4 = time()
        print(f'build query sets: {t4 - t3}')

        in_progress_accs = set(list(query_set_in_progress))
        completed_accs = set(list(query_set_complete))
        errored_accs = set(list(query_set_error))

        t5 = time()
        print(f'Create sets: {t5 - t4}')

        if request.user.is_authenticated:
            username = request.user.username

            # Add record in history table
            history = History(user_id=username,
                              time_stamp=datetime.now().strftime("%m/%d/%Y, %H:%M:%S"),
                              assay_type=utils.stringify_list(search_criteria.get('assay_type', None)),
                              bioproject=utils.stringify_list(search_criteria.get('bioproject', None)),
                              biosample=utils.stringify_list(search_criteria.get('biosample', None)),
                              breed_sam=utils.stringify_list(search_criteria.get('breed_sam', None)),
                              center_name=utils.stringify_list(search_criteria.get('center_name', None)),
                              country=utils.stringify_list(search_criteria.get('geo_loc_name_country_calc', None)),
                              continent=utils.stringify_list(search_criteria.get('geo_loc_name_country_continent_calc', None)),
                              cultivar_sam=utils.stringify_list(search_criteria.get('cultivar_sam', None)),
                              ecotype_same=utils.stringify_list(search_criteria.get('ecotype_same', None)),
                              experiment_name=utils.stringify_list(search_criteria.get('experiment', None)),
                              gender=utils.stringify_list(search_criteria.get('gender', None)),
                              isolate_sam=utils.stringify_list(search_criteria.get('isolate_sam', None)),
                              library_layout=utils.stringify_list(search_criteria.get('librarylayout', None)),
                              library_selection=utils.stringify_list(search_criteria.get('library_selection', None)),
                              organism=utils.stringify_list(search_criteria.get('organism', None)),
                              sample_acc=utils.stringify_list(search_criteria.get('sample_acc', None)),
                              sra_study=utils.stringify_list(search_criteria.get('sra_study', None)),
                              strain_sam=utils.stringify_list(search_criteria.get('strain_sam', None)))
            history.save()
        else:
            username = None
        sel_runIds_visual = request.session.get(session_key_visual, [])

        t6 = time()
        print(f'Built history: {t6 - t5}')

        return render(request, 'table.html', {'metadata': page_object,
                                              'in_progress_accs': in_progress_accs,
                                              'completed_accs': completed_accs,
                                              'errored_accs': errored_accs,
                                              'username': username,
                                              'order_by': order_by,
                                              'direction': direction,
                                              'num_records': num_records,
                                              'selected_visual': sel_runIds_visual,
                                              'selected_visual_records': len(sel_runIds_visual),
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

        sel_runIds_visual = request.session.get(session_key_visual, [])

        return render(request, 'table.html', {'metadata': page_object,
                                              'in_progress_accs': in_progress_accs,
                                              'completed_accs': completed_accs,
                                              'errored_accs': errored_accs,
                                              'username': username,
                                              'order_by': order_by,
                                              'direction': direction,
                                              'num_records': num_records,
                                              'selected_visual': sel_runIds_visual,
                                              'selected_visual_records' : len(sel_runIds_visual),
                                              'search_criteria': json.dumps(search_criteria)})








    else:
        return render(request, 'page_not_found.html')


def populate_home_page(request, search_id):

    search_record = History.objects.get(search_id=search_id)

    if not search_record:
        return render(request, "page_not_found.html")

    form = MetadataForm()

    # Clear the form
    form.fields['librarylayout'].initial = ''
    form.fields['sra_study'].initial = ''
    form.fields['center_name'].initial = ''
    form.fields['experiment'].initial = ''
    form.fields['sample_acc'].initial = ''
    form.fields['biosample'].initial = ''
    form.fields['organism'].initial = ''
    form.fields['bioproject'].initial = ''
    form.fields['geo_loc_name_country_calc'].initial = ''
    form.fields['geo_loc_name_country_continent_calc'].initial = ''

    # Populate the form
    if search_record.library_layout is not None:
        form.fields['librarylayout'].initial = search_record.library_layout.split(',')

    if search_record.sra_study is not None:
        form.fields['sra_study'].initial = search_record.sra_study.split(',')

    if search_record.center_name is not None:
        form.fields['center_name'].initial = search_record.center_name.split(',')

    if search_record.experiment_name is not None:
        form.fields['experiment'].initial = search_record.experiment_name.split(',')

    if search_record.sample_acc is not None:
        form.fields['sample_acc'].initial = search_record.sample_acc.split(',')

    if search_record.biosample is not None:
        form.fields['biosample'].initial = search_record.biosample.split(',')

    if search_record.organism is not None:
        form.fields['organism'].initial = search_record.organism.split(',')

    if search_record.bioproject is not None:
        form.fields['bioproject'].initial = search_record.bioproject.split(',')

    if search_record.country is not None:
        form.fields['geo_loc_name_country_calc'].initial = search_record.country.split(',')

    if search_record.continent is not None:
        form.fields['geo_loc_name_country_continent_calc'].initial = search_record.continent.split(',')

    return render(request, "home.html", {"form": form})


@login_required(login_url="login")
def set_email_notification(request):
    if request.method == "PUT":
        # Get the form data
        data = json.loads(request.body)
        receive_email = data.get("receiveEmail", None)
        if receive_email is None:
            return JsonResponse({"success": False, "message": "Invalid request!"})

        user = User.objects.get(username=request.user.username)
        user.email_notification = receive_email
        user.save()

        # Update the status table
        Status.objects.filter(user_id=user.username).update(email_notification=receive_email)

        if receive_email:
            return JsonResponse({"success": True, "message": "You will receive email notifications."})
        else:
            return JsonResponse({"success": True, "message": "You will no longer receive email notifications."})

    else:
        return JsonResponse({"success": False, "message": "Invalid request!"})
