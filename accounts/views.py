from django.shortcuts import render
from rest_framework.views import APIView, Response, status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class RegisterAPIView(APIView):
    def post(self, request):
        username = request.data['username']
        password = request.data['password']

        if not (username and password):
            return Response(data={"message": "Some fields are not filled in!"}, status=status.HTTP_400_BAD_REQUEST)
        
        user = User.objects.filter(username=username)
        if user.exists():
            return Response(data={"message": "Such user already exists!"}, status=status.HTTP_409_CONFLICT)
        
        user = User.objects.create_user(username=username, password=password)
        token, _ = Token.objects.create(user=user)
        
        return Response(data={"token": token.key}, status=status.HTTP_201_CREATED)


class LoginAPIView(APIView):
    def post(self, request):
        username = request.data['username']
        password = request.data['password']

        if not (username and password):
            return Response(data={"message": "Some fields are not filled in!"}, status=status.HTTP_400_BAD_REQUEST)
        
        user = User.objects.filter(username=username)
        if not user.exists():
            return Response(data={"message": "Such user does not exist!"}, status=status.HTTP_404_NOT_FOUND)
        
        user = user.first()
        if not user.check_password(password):
            return Response(data={"message": "Invalid password!"}, status=status.HTTP_401_UNAUTHORIZED)
        
        token, _ = Token.objects.get(user=user) # Add checking for token existence
        return Response(data={"token": token.key}, status=status.HTTP_200_OK)


def login(request):
    if request.method == "GET":
        return render(request, "accounts/login.html")


def signup(request):
    if request.method == "GET":
        return render(request, "accounts/signup.html")
