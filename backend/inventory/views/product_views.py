from rest_framework.viewsets import ModelViewSet
from inventroy.models.product_model import Product
from inventroy.serializers.product_serializer import ProductSerializer
from users.permissions.user_permissions import IsAdmin, IsManager, IsEmployee, IsViewer
from authentication.custom_jwt.custom_jwt import CustomJWTAuthentication
from rest_framework.permissions import IsAuthenticated
from loguru import logger


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all().order_by("-created_at")
    serializer_class = ProductSerializer
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
        try:
            serializer.save()
            logger.info(
                f"Product '{serializer.instance.name}' created by '{self.request.user.email}'."
            )
        except Exception as e:
            logger.error(
                f"Failed to create product with data {serializer.validated_data} by '{self.request.user.email}'. Error: {str(e)}"
            )
            raise

    def perform_update(self, serializer):
        try:
            serializer.save()
            logger.info(
                f"Product '{serializer.instance.name}' updated by '{self.request.user.email}'."
            )
        except Exception as e:
            logger.error(
                f"Failed to update product with data {serializer.validated_data} by '{self.request.user.email}'. Error: {str(e)}"
            )
            raise

    def perform_destroy(self, instance):
        name = instance.name
        try:
            instance.delete()
            logger.info(f"Product '{name}' deleted by '{self.request.user.email}'.")
        except Exception as e:
            logger.error(
                f"Failed to delete product '{name}' by '{self.request.user.email}'. Error: {str(e)}"
            )
            raise
