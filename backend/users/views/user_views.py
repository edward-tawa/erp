from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from authentication.custom_jwt.custom_jwt import CustomJWTAuthentication
from users.permissions.user_permissions import IsAdmin, IsManager, IsEmployee, IsViewer
from django.contrib.auth import get_user_model
from users.serializers.user_serializer import UserSerializer
from loguru import logger


User = get_user_model()


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [CustomJWTAuthentication]

    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            # Create/Update/Delete: Authenticated AND (Admin OR Manager)
            return [IsAuthenticated(), IsAdmin() | IsManager()]

        elif self.action in ["list", "retrieve"]:
            # List/Retrieve: Authenticated AND (any role)
            return [
                IsAuthenticated(),
                IsAdmin() | IsManager() | IsEmployee() | IsViewer(),
            ]

        else:
            return [IsAuthenticated()]

    def perform_create(self, serializer):
        serializer.save()
        logger.info(
            f"User '{serializer.instance.email}' created by '{self.request.user.email}'."
        )

    def perform_update(self, serializer):
        serializer.save()
        logger.info(
            f"User '{serializer.instance.email}' updated by '{self.request.user.email}'."
        )

    def perform_destroy(self, instance):
        email = instance.email
        instance.delete()
        logger.info(f"User '{email}' deleted by '{self.request.user.email}'.")
