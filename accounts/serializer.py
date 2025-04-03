from django.contrib.auth.models import User
from rest_framework import serializers
import pdb


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "password")
        read_only_fields = ("id",)


class UserLoginSerializer(UserSerializer):
    def validate(self, attrs):
        print(f"Полученные данные: {attrs}")
        user = User.objects.filter(username=attrs.get("username")).first()
        if not user:
            raise serializers.ValidationError("Such user does not exist!")
        
        is_passwd_valid = user.check_password(attrs.get("password"))
        if not is_passwd_valid:
            raise serializers.ValidationError("Invalid password!")
        
        print(f"Авторизованный пользователь: {user}")
        attrs["user"] = user 
        return attrs


class UserCreateSerializer(UserSerializer):
    confirm_password = serializers.CharField(write_only=True)

    class Meta(UserSerializer.Meta):
        fields = UserSerializer.Meta.fields + ("confirm_password",)

    def validate(self, attrs):
        if attrs.get("password") != attrs.get("confirm_password"):
            raise serializers.ValidationError("Passwords must be the same!")

        return attrs
    
    def create(self, validated_data):
        validated_data.pop("confirm_password")

        username = validated_data["username"]
        if not User.objects.filter(username=username).exists():
            raise serializers.ValidationError("Such user already exists!")
        
        user = User.objects.create_user(username=username, password=validated_data["password"])
        return user
