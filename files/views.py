from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers.file_serializer import (
    FileCreateSerializer,
    FileReadSerializer,
    FileSerializer,
    FileDeleteSerializer,
)
from .models import File
from rest_framework.parsers import MultiPartParser


class FileViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser]
    serializer_class = FileSerializer

    def get_queryset(self):
        return File.objects.filter(user=self.request.user).all()

    def get_serializer_class(self):
        serializer_map = {
            "create": FileCreateSerializer,
            "list": FileReadSerializer,
            "destroy": FileDeleteSerializer,
        }
        return serializer_map.get(self.action, super().get_serializer_class())


def download(request):
    if request.method == "GET":
        return render(request, "files/download.html")


def upload(request):
    if request.method == "GET":
        return render(request, "files/upload.html")


def list(request):
    if request.method == "GET":
        return render(request, "files/list.html")
