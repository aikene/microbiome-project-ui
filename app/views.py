import logging
import urllib.parse

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

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
