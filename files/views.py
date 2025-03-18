from django.shortcuts import render
from rest_framework import viewsets


class FileViewSet(viewsets.ModelViewSet):
    pass

def get_file(request):
    if request.method == "GET":
        return render(request, "files/get_file.html")


def upload_file(request):
    if request.method == "GET":
        return render(request, "files/upload_file.html")
