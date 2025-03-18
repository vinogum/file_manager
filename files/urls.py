from rest_framework import routers
from .views import FileViewSet
from django.urls import path, include
from . import views

router = routers.DefaultRouter()
router.register(r"files", FileViewSet)

urlpatterns = [
    path("", views.upload_file, name="upload-file"),
    path("get-file/", views.get_file, name="get-file"),

    # API views
    path("api/", include(router.urls)),
]
