from django.urls import path

from . import views

app_name = "auth"

urlpatterns = [
    path("register/", views.ArticleListView.as_view(), name="register"),
    path("login/", views.ContactCreateView.as_view(), name="login"),
]
