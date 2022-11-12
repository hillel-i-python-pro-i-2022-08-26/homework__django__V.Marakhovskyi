from django.urls import path

from . import views

app_name = "contacts"

urlpatterns = [
    path("", views.ArticleListView.as_view(), name="read"),
    path("form/", views.ContactCreateView.as_view(), name="create"),
    # path("form/", views.crud_contacts, name="create"),
    path("delete/<int:pk>/", views.contact_delete, name="delete"),
    # path("update/<int:pk>/", views.update_contact, name="update"),
    path("update/<int:pk>/", views.ContactUpdateView.as_view(), name="update"),
]
