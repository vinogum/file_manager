from django.shortcuts import render
from rest_framework.views import Response, status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from .serializer import UserCreateSerializer, UserLoginSerializer
from rest_framework.generics import CreateAPIView
import pdb


class RegisterAPIView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserCreateSerializer


class LoginAPIView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserLoginSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, _ = Token.objects.get_or_create(user=user)
        return Response(data={"token": token.key, "user": serializer.data}, status=status.HTTP_200_OK)


def login(request):
    if request.method == "GET":
        return render(request, "accounts/login.html")


def signup(request):
    if request.method == "GET":
        return render(request, "accounts/signup.html")
