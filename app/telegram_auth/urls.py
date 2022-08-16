from django.urls import path, include
from rest_framework.routers import DefaultRouter

from app.telegram_auth.api import AuthLoginView

urlpatterns = [
    path("", AuthLoginView.as_view(), name="auth-login"),
]
