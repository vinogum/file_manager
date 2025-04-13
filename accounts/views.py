from rest_framework.views import APIView, Response, status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializer import UserCreateSerializer, UserLoginSerializer
from rest_framework.generics import CreateAPIView
from rest_framework.parsers import MultiPartParser


class RegisterAPIView(CreateAPIView):
    permission_classes = [AllowAny]
    parser_classes = [MultiPartParser]
    serializer_class = UserCreateSerializer


class LoginAPIView(CreateAPIView):
    permission_classes = [AllowAny]
    parser_classes = [MultiPartParser]
    serializer_class = UserLoginSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, _ = Token.objects.get_or_create(user=user)
        return Response(
            data={"token": token.key, "user": serializer.data},
            status=status.HTTP_200_OK,
        )


class LogoutAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            token = Token.objects.get(user=request.user)
            token.delete()
            return Response(status=status.HTTP_200_OK)
        except Token.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
