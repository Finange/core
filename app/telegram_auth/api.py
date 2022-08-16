from rest_framework.decorators import action
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from app.telegram_auth.models import TelegramUser
from app.telegram_auth.serializers import AuthSerializer


class AuthLoginView(CreateAPIView):
    serializer_class = AuthSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        validated_data = serializer.validated_data

        telegram_user, created = TelegramUser.objects.get_or_create(
            telegram_id=validated_data.get("id")
        )

        refresh = RefreshToken.for_user(telegram_user)

        return Response({"refresh": str(refresh), "access": str(refresh.access_token)})
