from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect, resolve_url
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from apps.register.forms import SignUpForm
from apps.users.models import User
from core import settings


# def auth(request):
#     if request.method == "POST":
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             messages.success(request, "Registration successful")
#             return redirect("index")
#         else:
#             messages.error(request, "Registration failed")
#     else:
#         form = SignUpForm()
#     return render(request, "auth/auth.html", {"form": form})


class RegisterUser(CreateView):
    form_class = SignUpForm
    template_name = "auth/register.html"
    success_url = reverse_lazy("index")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Register"
        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        messages.success(self.request, "Registration successful")
        return redirect("index")


# def user_login(request):
#     if request.method == "POST":
#         form = UserLoginForm(data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             return redirect("greetings:greet")
#     else:
#         form = UserLoginForm()
#     return render(request, "auth/login.html", {"form": form})


class UserLogin(LoginView):
    form_class = AuthenticationForm
    template_name = "auth/login.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Log In"
        return context

    def get_success_url(self):
        return reverse_lazy("index")


# def user_logout(request):
#     logout(request)
#     return redirect("auth:login")


class UserLogout(LogoutView):
    def get_default_redirect_url(self):
        """Return the default redirect URL."""
        if self.next_page:
            return resolve_url(self.next_page)
        elif settings.LOGOUT_REDIRECT_URL:
            return resolve_url(settings.LOGOUT_REDIRECT_URL)
        else:
            return self.request.path


class UserEditView(UpdateView):
    # form_class = UserEditForm
    model = User
    fields = (
        "username",
        "email",
        "avatar",
    )
    template_name = "auth/user_edit_form.html"
    template_name_suffix = "_edit_form"
    success_url = reverse_lazy("index")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Edit user"
        return context

    def get_object(self):
        return self.request.user
