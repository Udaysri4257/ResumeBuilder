from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from accounts.forms import LogInForm, SignUpForm
from django.contrib.auth.models import User


# Create your views here.


def user_login(request):
    if request.method == "POST":
        form = LogInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                form.add_error(None, "Incorrect Login Details")

    else:
        form = LogInForm()
    context = {
        "form": form,
    }
    return render(request, "accounts/login.html", context)


def log_out(request):
    logout(request)
    return redirect("login")


def sign_up(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            password_confirmation = form.cleaned_data["password_confirmation"]

            if password == password_confirmation:
                user = User.objects.create_user(username, password=password)
                login(request, user)
                return redirect("login")
            else:
                form.add_error(None, "Passwords do not match")
    else:
        form = SignUpForm()
    context = {
        "form": form,
    }
    return render(request, "registration/signup.html", context)
