from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from apps.register.forms import SignUpForm


# def register(request):
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
#     return render(request, "auth/register.html", {"form": form})


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


def user_logout(request):
    logout(request)
    return redirect("auth:login")
