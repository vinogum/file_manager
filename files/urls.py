from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedDefaultRouter
from .views import FileViewSet


files_router = DefaultRouter()
files_router.register(r"files", FileViewSet, basename="file")
versions_router = NestedDefaultRouter(files_router, r"files", lookup="file")
versions_router.register(r"versions", FileViewSet, basename="file-versions")


urlpatterns = files_router.urls + versions_router.urls
