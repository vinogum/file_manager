from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedDefaultRouter
from .views import FileViewSet
from django.urls import path, include
from . import views


files_router = DefaultRouter()
files_router.register(r"files", FileViewSet)

urlpatterns = [
    # Standalone views
    path("upload/", views.upload, name="upload"),
    path("download/", views.download, name="download"),

    # API endpoints (DRF routers)
    path("api/", include(files_router.urls)),
]
