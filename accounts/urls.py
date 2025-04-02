from django.urls import path
from . import views

urlpatterns = [
    # Views
    path("login/", views.login, name="login"),
    path("signup/", views.signup, name="signup"),
    # API
    path("api/signup/", views.RegisterAPIView.as_view()),
    path("api/login/", views.LoginAPIView.as_view()),
]
