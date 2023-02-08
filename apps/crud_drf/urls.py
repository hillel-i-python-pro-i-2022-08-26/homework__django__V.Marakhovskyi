from django.urls import path

from .views import ContactAPIView

# router = routers.DefaultRouter()
# router.register(r'contacts', views.ContactViewSet)

urlpatterns = [
    path("general/", ContactAPIView.as_view()),
    # path('update/<int:pk>/', ContactUpdateApi.as_view()),
    # path('show/<int:pk>/', ContactViewApi.as_view()),
    # path('delete/<int:pk>/', ContactDeleteApi.as_view()),
]
