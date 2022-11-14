from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from apps.register.forms import SignUpForm


# from apps.register.forms import UserCustomForm


def register(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful")
            return redirect("auth:login")
        else:
            messages.error(request, "Registration failed")
    else:
        form = UserCreationForm()
    return render(request, "auth/register.html", {"form": form})


def login(request):
    return render(request, "auth/login.html")
