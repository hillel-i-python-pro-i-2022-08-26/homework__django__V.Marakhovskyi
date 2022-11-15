from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from apps.users.models import User


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        label="Username",
        help_text="Length should be not more than 32 characters",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={"class": "form-control"}))
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password2 = forms.CharField(label="Confirm password", widget=forms.PasswordInput(attrs={"class": "form-control"}))
    avatar = forms.ImageField(label="Avatar")

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2", "avatar")


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={"class": "form-control"}))
