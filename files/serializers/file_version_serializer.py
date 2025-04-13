from ..models import FileVersion
from rest_framework import serializers


class FileVersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileVersion
        fields = "__all__"
        read_only_fields = ("id", "version", "uploaded_at")


class FileVersionReadSerializer(FileVersionSerializer):
    file = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta(FileVersionSerializer.Meta):
        exclude = ("file_data",)
