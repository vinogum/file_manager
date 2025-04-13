from django.contrib.auth.models import User
from rest_framework import serializers


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ("id", "username", "password", "confirm_password")
        read_only_fields = ("id",)

    def validate(self, attrs):
        if attrs.get("password") != attrs.get("confirm_password"):
            raise serializers.ValidationError("Passwords must be the same!")

        return attrs

    def create(self, validated_data):
        validated_data.pop("confirm_password")

        username = validated_data["username"]
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError("Such user already exists!")

        user = User.objects.create_user(
            username=username, password=validated_data["password"]
        )
        return user
