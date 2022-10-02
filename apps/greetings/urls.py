from django.urls import path

from . import views

urlpatterns = [
    path("<str:name>", views.greetings_view, name="personality"),
    path("", views.greetings_view, name="index"),
]
