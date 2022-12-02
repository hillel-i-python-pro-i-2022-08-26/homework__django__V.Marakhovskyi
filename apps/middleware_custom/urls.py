from django.urls import path

from apps.middleware_custom import views

app_name = "middleware"

urlpatterns = [
    path("", views.AllInfoView.as_view(), name="all_info"),
]
