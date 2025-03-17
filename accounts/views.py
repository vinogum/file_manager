from django.shortcuts import render
from rest_framework.views import APIView, Response, status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny


class RegisterAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        confirm_password = request.data.get("confirm-password")

        if "" in [username, password, confirm_password]:
            return Response(data={"message": "Some fields are not filled in!"}, status=status.HTTP_400_BAD_REQUEST)
        
        is_passwds_match = (password == confirm_password)
        if not is_passwds_match:
            return Response(data={"message": "Passwords do not match!"}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.filter(username=username)
        if user.exists():
            return Response(data={"message": "Such user already exists!"}, status=status.HTTP_409_CONFLICT)
        
        User.objects.create_user(username=username, password=password)
        
        return Response(data={"message": "Successful registration!"}, status=status.HTTP_201_CREATED)


class LoginAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        if not (username and password):
            return Response(data={"message": "Some fields are not filled in!"}, status=status.HTTP_400_BAD_REQUEST)
        
        user = User.objects.filter(username=username)
        if not user.exists():
            return Response(data={"message": "Such user does not exist!"}, status=status.HTTP_404_NOT_FOUND)
        
        user = user.first()
        if not user.check_password(password):
            return Response(data={"message": "Invalid password!"}, status=status.HTTP_401_UNAUTHORIZED)
        
        token, _ = Token.objects.get_or_create(user=user)
        return Response(data={"message": "Successful ", "token": token.key}, status=status.HTTP_200_OK)


def login(request):
    if request.method == "GET":
        return render(request, "accounts/login.html")


def signup(request):
    if request.method == "GET":
        return render(request, "accounts/signup.html")
