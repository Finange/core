from django.contrib.auth.base_user import (
    BaseUserManager as DefaultBaseUserManager,
    AbstractBaseUser,
)
from django.contrib.auth.models import AbstractUser
from django.db import models, transaction

from django.utils.translation import gettext_lazy as _

# Create your models here.


class BaseUserManager(DefaultBaseUserManager):
    def _create_user(self, telegram_id, **extra_fields):
        """
        If the telegram_id is not set, raise a ValueError. Otherwise, create a user with the telegram_id and any extra
        fields passed in

        :param telegram_id: The unique identifier for the user
        :return: The user object.
        """
        if not telegram_id:
            raise ValueError(_("The telegram_id must be set"))
        user = self.model(telegram_id=telegram_id, **extra_fields)
        user.save(using=self._db)
        return user

    def create_user(self, telegram_id, **extra_fields):
        """
        It creates a user with the given telegram_id and extra_fields

        :param telegram_id: The unique identifier of the user
        :return: The user object.
        """
        return self._create_user(telegram_id, **extra_fields)

    @transaction.atomic
    def get_or_create(self, telegram_id, **kwargs):
        """
        If a user with the given telegram_id exists, return that user, otherwise create a new user with the given
        telegram_id and return that user

        :param telegram_id: The unique identifier for the user
        :return: The user object and a boolean value.
        """
        user = self.filter(telegram_id=telegram_id).first()

        if user:
            return user, False

        return self.create_user(telegram_id=telegram_id, **kwargs), True


class TelegramUser(AbstractBaseUser):
    telegram_id = models.IntegerField(null=True, blank=True, unique=True)
    joined_at = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = "telegram_id"
    REQUIRED_FIELDS = []

    objects = BaseUserManager()

    class Meta:
        verbose_name = _("Telegram User")
        verbose_name_plural = _("Telegram Users")
