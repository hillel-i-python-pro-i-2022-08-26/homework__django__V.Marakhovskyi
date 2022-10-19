from django.urls import path

from . import views

app_name = "session_info"

urlpatterns = [
    path("", views.session_view, name="index"),
]
