from django.urls import path

from . import views

app_name = "auth"

urlpatterns = [
    # path("auth/", views.auth, name="auth"),
    path("auth/", views.RegisterUser.as_view(), name="auth"),
    # path("login/", views.user_login, name="login"),
    path("login/", views.UserLogin.as_view(), name="login"),
    # path("logout/", views.user_logout, name="logout"),
    path("logout/", views.UserLogout.as_view(), name="logout"),
    path("settings/<int:pk>/", views.UserEditView.as_view(), name="settings"),
]
