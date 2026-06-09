from django.contrib.auth.models import ModelBackend
from django.core.exceptions import MultipleObjectsReturned
from django.contrib.auth import get_user_model
from django.db import Q
from loguru import logger

User = get_user_model()


class LoginBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        if not username or not password:
            return None

        try:
            user = User.objects.get(Q(email=username) | Q(username=username))
        except User.DoesNotExist:
            logger.warning(f"Login failed: No user found with '{username}'")
            return None
        except MultipleObjectsReturned:
            logger.error(f"Multiple users found with '{username}'")
            return None

        if not user.check_password(password):
            logger.warning(f"Login failed: Invalid password for '{username}'")
            return None

        if not user.is_active:
            logger.warning(f"Login failed: Inactive account '{username}'")
            return None

        logger.info(f"User '{user.email}' logged in successfully")
        return user
