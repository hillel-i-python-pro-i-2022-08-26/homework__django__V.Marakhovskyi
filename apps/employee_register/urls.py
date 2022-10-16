from django.urls import path

from . import views

app_name = "employee_register"

urlpatterns = [
    path("", views.employee_form, name="insert"),  # get and post req. for insert operation
    path("<int:id>/", views.employee_form, name="update"),  # get and post req. for update operation
    path("list/", views.employee_list, name="list"),  # get req. to retrieve and display all records
    path("delete/<int:id>/", views.employee_delete, name="delete"),
]
