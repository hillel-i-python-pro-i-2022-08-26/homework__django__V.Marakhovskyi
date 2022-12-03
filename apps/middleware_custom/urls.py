from django.urls import path

from apps.middleware_custom import views

app_name = "middleware"

urlpatterns = [
    path("", views.AllInfoView.as_view(), name="all_info"),
    path("exact_session/", views.ExactSessionView.as_view(), name="session_info"),
    path("exact_user/", views.ExactUserView.as_view(), name="user_info"),
]
