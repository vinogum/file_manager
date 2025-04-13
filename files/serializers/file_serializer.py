from ..models import File, FileVersion
from rest_framework import serializers


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ("id", "user", "url")
        read_only_fields = ("id", "user")


class FileCreateSerializer(FileSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    file_data = serializers.FileField(write_only=True)

    class Meta(FileSerializer.Meta):
        fields = FileSerializer.Meta.fields + ("file_data",)

    def create(self, validated_data):
        user = self.context["request"].user
        url = validated_data["url"]
        file_data = validated_data["file_data"]

        file, _ = File.objects.get_or_create(user=user, url=url)

        FileVersion.objects.create(file=file, file_data=file_data)
        return file


class FileReadSerializer(FileSerializer):
    class Meta(FileSerializer.Meta):
        read_only_fields = FileSerializer.Meta.fields


class FileDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ("id",)
