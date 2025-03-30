from ..models import FileVersion
from rest_framework import serializers


class FileVersionSerializer(serializers.ModelSerializer):
    version = serializers.IntegerField(read_only=True)
    uploaded_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = FileVersion
        fields = "__all__"
