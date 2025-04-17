from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers.file_serializer import (
    FileCreateSerializer,
    FileReadSerializer,
    FileSerializer,
)
from .serializers.file_version_serializer import (
    FileVersionSerializer,
    FileVersionReadSerializer,
)
from .models import File, FileVersion
from rest_framework.parsers import MultiPartParser
from django.http import FileResponse


class FileViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser]
    serializer_class = FileSerializer

    def get_queryset(self):
        return File.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        serializer_map = {
            "create": FileCreateSerializer,
            "list": FileReadSerializer,
        }
        return serializer_map.get(self.action, super().get_serializer_class())


class FileVersionViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser]
    serializer_class = FileVersionSerializer

    def get_queryset(self):
        file_id = self.kwargs.get("file_pk")
        return FileVersion.objects.filter(file_id=file_id)

    def get_serializer_class(self):
        serializer_map = {
            "list": FileVersionReadSerializer,
        }
        return serializer_map.get(self.action, super().get_serializer_class())

    def retrieve(self, request, *args, **kwargs):
        version = self.get_object()
        return FileResponse(
            version.file_data, as_attachment=True, filename=version.file_data.name
        )
