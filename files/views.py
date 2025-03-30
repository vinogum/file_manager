from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers.file_serializer import WriteFileSerializer
from .models import File
from rest_framework.parsers import MultiPartParser


class FileViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser]
    queryset = File.objects.all()

    def get_serializer_class(self):
        if self.action == "create":
            return WriteFileSerializer
        return super().get_serializer_class()
    
    def get_serializer_context(self):
        return super().get_serializer_context()


def download(request):
    if request.method == "GET":
        return render(request, "files/download.html")


def upload(request):
    if request.method == "GET":
        return render(request, "files/upload.html")
