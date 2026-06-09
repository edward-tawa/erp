from rest_framework.viewsets import ModelViewSet
from inventroy.models.stock_take_model import StockTake
from inventroy.serializers.stock_take_serializer import StockTakeSerializer
from users.permissions.user_permissions import IsAdmin, IsManager, IsEmployee, IsViewer
from authentication.custom_jwt.custom_jwt import CustomJWTAuthentication
from rest_framework.permissions import IsAuthenticated
from loguru import logger


class StockTakeViewSet(ModelViewSet):
    queryset = StockTake.objects.select_related("product").order_by("-created_at")
    serializer_class = StockTakeSerializer
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
                f"StockTake for product '{serializer.instance.product.name}' created by '{self.request.user.email}'."
            )
        except Exception as e:
            logger.error(
                f"Failed to create StockTake with data {serializer.validated_data} by '{self.request.user.email}'. Error: {str(e)}"
            )
            raise

    def perform_update(self, serializer):
        try:
            serializer.save()
            logger.info(
                f"StockTake for product '{serializer.instance.product.name}' updated by '{self.request.user.email}'."
            )
        except Exception as e:
            logger.error(
                f"Failed to update StockTake with data {serializer.validated_data} by '{self.request.user.email}'. Error: {str(e)}"
            )
            raise

    def perform_destroy(self, instance):
        product_name = instance.product.name
        try:
            instance.delete()
            logger.info(
                f"StockTake for product '{product_name}' deleted by '{self.request.user.email}'."
            )
        except Exception as e:
            logger.error(
                f"Failed to delete StockTake for product '{product_name}' by '{self.request.user.email}'. Error: {str(e)}"
            )
            raise
