from django.contrib import messages
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect

from apps.register.forms import SignUpForm, UserLoginForm


def register(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful")
            return redirect("index")
        else:
            messages.error(request, "Registration failed")
    else:
        form = SignUpForm()
    return render(request, "auth/register.html", {"form": form})


def user_login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("greetings:greet")
    else:
        form = UserLoginForm()
    return render(request, "auth/login.html", {"form": form})


def user_logout(request):
    logout(request)
    return redirect("auth:login")
