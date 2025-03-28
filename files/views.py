from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import FileVersionSerializer
from .models import FileVersion, File
from rest_framework.response import Response
from rest_framework import status


class FileViewSet(viewsets.ModelViewSet):
    queryset = FileVersion.objects.all()
    serializer_class = FileVersionSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        file, _ = File.objects.get_or_create(user=request.user, url=request.data.get("url"))

        data = {"file": file.id, "file_data": request.data.get("file")}

        file_version_serializer = self.get_serializer(data=data)
        file_version_serializer.is_valid(raise_exception=True)
        self.perform_create(file_version_serializer)

        return Response(data={"message": "File has successfully created!"}, status=status.HTTP_201_CREATED)


def get_file(request):
    if request.method == "GET":
        return render(request, "files/get_file.html")


def upload_file(request):
    if request.method == "GET":
        return render(request, "files/upload_file.html")
