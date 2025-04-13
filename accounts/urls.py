from django.urls import path, include
from . import views


urlpatterns = [
    path("", include("rest_framework.urls")),
    path("signup/", views.RegisterAPIView.as_view()),
]
