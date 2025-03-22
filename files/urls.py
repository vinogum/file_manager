from rest_framework import routers
from .views import FileViewSet
from django.urls import path, include
from . import views

router = routers.DefaultRouter()
router.register(r"files", FileViewSet)

urlpatterns = [
    path("upload/", views.upload_file, name="upload_file"),
    path("get/", views.get_file, name="get_file"),

    # API views
    path("api/", include(router.urls)),
]
