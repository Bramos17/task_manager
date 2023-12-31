from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from accounts.forms import LoginForm, SignUpForm


def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")
    else:
        form = LoginForm()
    context = {"form": form}
    return render(request, "accounts/login.html", context)


def user_logout(request):
    logout(request)
    return redirect("login")


def user_signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            confirm = form.cleaned_data["password_confirmation"]
            if password == confirm:
                user = User.objects.create_user(
                    username=username, password=password
                )
                login(request, user)
                return redirect("list_projects")
            else:
                form.add_error(
                    "password_confirmation", "Passwords don't match"
                )
    else:
        form = SignUpForm()
        context = {"form": form}
    return render(request, "accounts/registration/signup.html", context)
