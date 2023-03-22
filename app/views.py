from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
import numpy as np

from .models import User


# Create your views here.


def home(request):
    other_list = ['buccal mucosa', 'blood cell', 'gingiva', 'nasal cavity', 'dorsum of tongue']
    for a in np.arange(1, 51):
        other_list.append(f'Other-{a}')
    list_of_filters = {
        'Host Characteristics': ['Male', 'Female', 'Disease State', 'Other'],
        'Sample Source': ['Feces', 'Skin', 'Cecum'],
        'Study Type': ['Metagenomics', '16S', 'Other'],
        'Other Criteria': other_list,
    }
    return render(request, 'home.html', {
        "filters": list_of_filters
    })


def visualization(request):
    return render(request, 'visualizations.html')


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
