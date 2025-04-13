from rest_framework.permissions import AllowAny
from rest_framework.generics import CreateAPIView
from rest_framework.parsers import MultiPartParser
from .serializer import UserCreateSerializer


class RegisterAPIView(CreateAPIView):
    permission_classes = [AllowAny]
    parser_classes = [MultiPartParser]
    serializer_class = UserCreateSerializer
