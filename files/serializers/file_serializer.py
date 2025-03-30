from ..models import File, FileVersion
from rest_framework import serializers


class WriteFileSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True, required=False)
    file_data = serializers.FileField(write_only=True)

    class Meta:
        model = File
        fields = ("user", "url", "file_data")

    def create(self, validated_data):
        user = self.context["request"].user
        url = validated_data["url"]
        file_data = validated_data["file_data"]

        file, _ = File.objects.get_or_create(user=user, url=url)

        FileVersion.objects.create(file=file, file_data=file_data)
        return file
