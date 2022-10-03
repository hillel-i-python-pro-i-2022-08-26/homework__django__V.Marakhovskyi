from django.urls import path

from . import views

app_name = "greetings"

urlpatterns = [
    path("<str:name>", views.greetings_view, name="personality"),
    path("", views.greetings_view, name="greet"),
]
