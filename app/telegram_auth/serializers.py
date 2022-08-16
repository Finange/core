import base64
import hashlib
import hmac

from django.conf import settings
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers


class AuthSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    auth_date = serializers.CharField(max_length=255)
    first_name = serializers.CharField(max_length=255)
    photo_url = serializers.URLField(allow_null=True)
    hash = serializers.CharField(max_length=255)
    username = serializers.CharField(max_length=255)

    BUILD_HASH_IGNORED_FIELDS = ["hash"]

    def authenticate(self, **kwargs):
        pass

    @staticmethod
    def verify_hash(check_string, user_hash):
        print(check_string.encode())
        secret_key = hashlib.sha256(settings.BOT_TOKEN.encode()).digest()
        dig = hmac.new(secret_key, check_string.encode(), hashlib.sha256).hexdigest()
        print(dig, user_hash)
        return dig == user_hash

    def build_hash_string(self, values):
        keys = sorted(values.keys())
        return "\n".join(
            f"{key}={values[key]}"
            for key in keys
            if key is not None and key not in self.BUILD_HASH_IGNORED_FIELDS
        )

    def validate(self, data):
        _id = data.get("id")
        user_hash = data.get("hash")

        if not self.verify_hash(
            self.build_hash_string(data),
            user_hash,
        ):
            raise serializers.ValidationError(_("Invalid hash"))

        return data
