import logging
import urllib.parse
import os
import boto3
import shutil
import psycopg2
import json

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.conf import settings
from django.views.generic import TemplateView
from zipfile import ZipFile
from datetime import datetime


from .models import User

# Create your views here.
logger = logging.getLogger('django')
parameters = {
    "library_layout": 'PAIRED'
}
s3_url = "https://qiime2storage.s3.us-west-2.amazonaws.com/merged_results"


def home(request):
    list_of_filters = {
        'Host Characteristics': ['Male', 'Female', 'Disease State', 'Other'],
        'Sample Source': ['Feces', 'Skin', 'Cecum'],
        'Study Type': ['Metagenomics', '16S', 'Other'],
        'Study ID': ['SRR12191591', 'ERR6005217', 'SRR12191683', 'SRR7646376', 'SRR7646363'],
        'Layout': ['Single', 'Paired']
    }
    return render(request, 'home.html', {
        "filters": list_of_filters
    })

def featuretable(request):
    return render(request,"featuretable.html")


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

def visualization(request):
    # response = requests.get(f"http://35.82.29.117:8000", params=parameters)
    # data = json.loads(response.content)
    # task_id = data['task_id']
    # timestamp = data['timestamp']
    task_id = ''
    timestamp = ''
    # logger.info(f"task_id = {task_id} \n timestamp = {timestamp}")
    #
    temp_url = f"{s3_url}/{timestamp}-{task_id}/"

    qiime_prefix = 'https://view.qiime2.org/visualization/?type=html&src='

    urls = {
        # 'Qiime Default Taxa Bar Plot': 'https://view.qiime2.org/visualization/?type=html&src=https%3A%2F%2Fdocs.qiime2.org%2F2021.8%2Fdata%2Ftutorials%2Fmoving-pictures%2Ftaxa-bar-plots.qzv',
        # 'Qiime Default Feature Table': 'https://view.qiime2.org/visualization/?type=html&src=https%3A%2F%2Fdocs.qiime2.org%2F2021.8%2Fdata%2Ftutorials%2Fmoving-pictures%2Ftable.qzv',
        # 'SRR12191591 Feature Table': f'{qiime_prefix}{urllib.parse.quote("https://mycorstestbucket574.s3.us-east-2.amazonaws.com/qiime-output/feature-table.qza".encode("utf8"), safe="")}',
        # 'SRR12191591 Taxonomy Artifact': f'{qiime_prefix}{urllib.parse.quote("https://mycorstestbucket574.s3.us-east-2.amazonaws.com/qiime-output/taxonomy.qza".encode("utf8"), safe="")}',
        # 'Demo Feature Table': f'{qiime_prefix}{urllib.parse.quote("https://mycorstestbucket574.s3.us-east-2.amazonaws.com/qiime-output/feature-table.qza".encode("utf8"), safe="")}',
        'Merged Feature Table': f'{qiime_prefix}{urllib.parse.quote(temp_url.encode("utf8"), safe="")}merged_feature_tables.qzv',
        'Merged Taxonomy Table': f'{qiime_prefix}{urllib.parse.quote(temp_url.encode("utf8"), safe="")}taxonomy_bar_plot.qzv',
    }

    return render(request, 'visualizations.html', {
        "urls": urls,
        "task_id": task_id,
    })

# API end point to get run status by run Id (/api/check_run_status/{runId})
def check_run_status(request,runId):

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
    cur.close()
    conn.close()
    if row:
        columns = [desc[0] for desc in cur.description]
        row_dict = dict(zip(columns, row))
        # Convert any datetime objects to strings
        for key, value in row_dict.items():
            if isinstance(value, datetime):
                row_dict[key] = value.strftime("%m/%d/%Y")
        json_data = json.dumps(row_dict)
        return HttpResponse(json_data, content_type='application/json')
    else:
        return HttpResponse(status=404)


def demo_table_view(request):
    return render(request,"demo_table_view.html")

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

def feature_table_summary(request,uuid):
    #uuid = request.GET.get('uuid', None)
    if uuid is not None and "demo" not in uuid:
        # Option 1) use shell command to copy files from s3 bucket to /app/static/visualization/
        # shutil.copytree('/home/qiime2/qiime2storage/merged_results/'+uuid+'/feature_table/','app/static/visualization/'+uuid+'/feature_table/')
        
        # Option 2) use boto3 to download files from s3 bucket
        # create an S3 client
        s3 = boto3.client('s3')

        # specify the S3 bucket and file names
        bucket_name = 'qiime2storage'
        qzv_file = 'merged_results/'+uuid+'/merged_feature_tables.qzv'

        # download the files from S3 and store them temporarily on the server
        target_folder= os.path.join(settings.BASE_DIR, 'app','static','visualization',uuid)
        if not os.path.exists(target_folder):
            os.makedirs(target_folder)
        s3.download_file(bucket_name, qzv_file, target_folder+"/merged_feature_tables.qzv")
        # unzip qzv file
        unzip( target_folder+"/merged_feature_tables.qzv",target_folder)

        # re-organize the folder
        move_data_folder(target_folder,'feature_table')

        return render(request,"feature_table_summary.html",{"chart_type": "live", "uuid":uuid})
    else:
        # show demo chart
        return render(request,"feature_table_summary.html",{"chart_type": "demo","uuid":"demo"})

def taxonomic_bar_plots(request,uuid):
    #uuid = request.GET.get('uuid', None)
    if uuid is not None and "demo" not in uuid:
        # Option 1) use shell command to copy files from s3 bucket to /app/static/visualization/
        # shutil.copytree('/home/qiime2/qiime2storage/merged_results/'+uuid+'/taxonomy_results/','app/static/visualization/'+uuid+'/taxonomy_results/')
        
        # Option 2) use boto3 to download files from s3 bucket
        # create an S3 client
        s3 = boto3.client('s3')

        # specify the S3 bucket and file names
        bucket_name = 'qiime2storage'
        qzv_file = 'merged_results/'+uuid+'/taxonomy_bar_plot.qzv'

        # download the files from S3 and store them temporarily on the server
        target_folder= os.path.join(settings.BASE_DIR, 'app','static','visualization',uuid)
        if not os.path.exists(target_folder):
            os.makedirs(target_folder)
        s3.download_file(bucket_name, qzv_file, target_folder+"/taxonomy_bar_plot.qzv")
        # unzip qzv file
        unzip( target_folder+"/taxonomy_bar_plot.qzv",target_folder)

        # re-organize the folder
        move_data_folder(target_folder,'taxonomy_results')

        return render(request,"taxonomic_bar_plots.html",{"chart_type": "live", "uuid":uuid})
    else:
        # show demo chart
        return render(request,"taxonomic_bar_plots.html",{"chart_type": "demo", "uuid":"demo"})
    

def generate_visualization(request):
    if request.method =='POST':
        # define the pattern for the checkbox names
        pattern = 'chk_'
        
        runIds = ""
        # loop through the request.POST dictionary to find the names of the checkboxes
        for name, value in request.POST.items():
            if name.startswith(pattern):
                # do something if the checkbox is checked
                runIds = runIds + " " + value
        
    return render(request,"visualization.html",{"runIds":runIds.strip()})

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

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.first_name = first_name
            user.last_name = last_name
            user.save()
        except IntegrityError:
            return render(request, "register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("home"))
    else:
        return render(request, "register.html")


@login_required(login_url="login")
def user_profile(request, username):
    username = User.objects.get(username=request.user)

    return render(request, "user_profile.html", {
        "username": username,
        "full_name": username.get_full_name,
        "email": username.email,
        "date_joined": username.date_joined,
    })
