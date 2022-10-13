from django.urls import path

from . import views

app_name = "contacts"

urlpatterns = [
    path("", views.get_contacts, name="index"),
    path("form/", views.crud_contacts, name="crud"),
]
