from rest_framework import routers

from .views import ContactViewSet, ContactAPICreate, ContactAPIRead, ContactAPIUpdate, ContactAPIDelete

router = routers.DefaultRouter()
router.register(r"contacts", ContactViewSet)

urlpatterns = [
    path("create/", ContactAPICreate.as_view()),
    path("read/<int:pk>/", ContactAPIRead.as_view()),
    path("update/<int:pk>/", ContactAPIUpdate.as_view()),
    path("delete/<int:pk>/", ContactAPIDelete.as_view()),
]
