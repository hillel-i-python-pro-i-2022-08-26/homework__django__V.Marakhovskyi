# from .views import ContactAPIView, ContactAPIUpdate, ContactAPIDetail, ContactViewSet
from rest_framework import routers

from .views import ContactViewSet

router = routers.DefaultRouter()
router.register(r"contacts", ContactViewSet)

urlpatterns = [
    # path("general/", ContactAPIView.as_view()),
    # path('update/<int:pk>/', ContactAPIUpdate.as_view()),
    # path('detail/<int:pk>/', ContactAPIDetail.as_view()),
    # path('', ContactViewSet.as_view({'get': 'list'})),
    # path('<int:pk>/', ContactViewSet.as_view({'put': 'update'})),
]
