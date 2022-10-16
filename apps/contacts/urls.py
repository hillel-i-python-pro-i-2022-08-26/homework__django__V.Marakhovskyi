from django.urls import path

from . import views

app_name = "contacts"

urlpatterns = [
    path("", views.get_contacts, name="index"),
    path("form/", views.crud_contacts, name="crud"),
    path("delete/<int:id>/", views.contact_delete, name="delete"),
    path("update/<int:id>/", views.update_contact, name="update"),
]
