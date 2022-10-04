from django.urls import path

from . import views

app_name = "greetings"

urlpatterns = [
    path("", views.greetings_view, name="greet"),
    path("<str:name>", views.greetings_view, name="greetname"),
]
