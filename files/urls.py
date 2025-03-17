from rest_framework import routers
from .views import FileViewSet
from django.urls import path, include
from . import views

router = routers.DefaultRouter()
router.register(r"files", FileViewSet)

urlpatterns = [
    path("get-file/", views.get_file, name="get-file"),
    path("upload-file/", views.upload_file, name="upload-file"),
    path("api/", include(router.urls)),
]
