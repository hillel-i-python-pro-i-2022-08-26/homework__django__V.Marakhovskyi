from django.urls import path

from . import views

app_name = "userdata"

urlpatterns = [
    path("", views.get_userlist, name="index"),
    path("<int:amount>", views.get_userlist, name="index"),
]
