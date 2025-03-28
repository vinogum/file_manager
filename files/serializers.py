from .models import File, FileVersion
from rest_framework import serializers


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = "__all__"


class FileVersionSerializer(serializers.ModelSerializer):
    version = serializers.IntegerField(read_only=True)
    uploaded_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = FileVersion
        fields = "__all__"
