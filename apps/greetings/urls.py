from django.urls import path

from . import views

urlpatterns = [
    path('<str:name>', views.url_greet_view, name='personality'), path('', views.default_greet_view, name='index')
]