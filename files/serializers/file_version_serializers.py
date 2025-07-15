from files.models import FileVersion
from rest_framework import serializers


class FileVersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileVersion
        fields = ("id", "file", "version", "uploaded_at")


class FileVersionReadSerializer(FileVersionSerializer):
    class Meta(FileVersionSerializer.Meta):
        read_only_fields = ("id", "file", "version", "uploaded_at")
