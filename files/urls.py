from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedDefaultRouter
from files.views import FileViewSet, FileVersionViewSet


files_router = DefaultRouter()
files_router.register(r"files", FileViewSet, basename="file")
versions_router = NestedDefaultRouter(files_router, r"files", lookup="file")
versions_router.register(r"versions", FileVersionViewSet, basename="file-versions")

urlpatterns = [
    path("", include(files_router.urls)),
    path("", include(versions_router.urls)),
]
