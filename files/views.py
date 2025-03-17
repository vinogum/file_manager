from django.shortcuts import render
from rest_framework import viewsets
from .models import File
from .serializer import FileSerializer
from rest_framework.permissions import IsAuthenticated


class FileViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        pass


def get_file(request):
    if request.method == "GET":
        return render(request, "files/get_file.html")


def upload_file(request):
    if request.method == "GET":
        return render(request, "files/upload_file.html")
