from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers.file_serializer import FileWriteSerializer, FileReadSerializer
from .models import File
from rest_framework.parsers import MultiPartParser


class FileViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser]

    def get_queryset(self):
        return File.objects.filter(user=self.request.user).all()

    def get_serializer_class(self):
        if self.action == "create":
            return FileWriteSerializer

        elif self.action == "list":
            return FileReadSerializer

        elif self.action == "delete":
            pass
        return super().get_serializer_class()


def download(request):
    if request.method == "GET":
        return render(request, "files/download.html")


def upload(request):
    if request.method == "GET":
        return render(request, "files/upload.html")


def list(request):
    if request.method == "GET":
        return render(request, "files/list.html")
