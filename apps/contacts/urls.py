from django.urls import path

from . import views

app_name = "contacts"

urlpatterns = [
    path("", views.get_contacts, name="read"),
    path("form/", views.crud_contacts, name="create"),
    path("delete/<int:pk>/", views.contact_delete, name="delete"),
    path("update/<int:pk>/", views.update_contact, name="update"),
]
