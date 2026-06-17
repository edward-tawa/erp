from rest_framework.viewsets import ModelViewSet
from sales.models.sales_order_item_model import SalesOrderItem
from sales.serializers.sales_order_item_serializer import SalesOrderItemSerializer
from users.permissions.user_permissions import IsEmployee, IsManager
from loguru import logger


class SalesOrderItemViewSet(ModelViewSet):
    queryset = SalesOrderItem.objects.all().order_by("-created_at")
    serializer_class = SalesOrderItemSerializer

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            permission_classes = [IsEmployee]
        else:
            permission_classes = [IsManager]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        sales_order_item = serializer.save()
        logger.info(
            f"Sales order item '{sales_order_item.id}' created successfully for product '{sales_order_item.product.name}' with quantity '{sales_order_item.quantity}'"
        )

    def perform_update(self, serializer):
        sales_order_item = serializer.save()
        logger.info(
            f"Sales order item '{sales_order_item.id}' updated successfully for product '{sales_order_item.product.name}' with quantity '{sales_order_item.quantity}'"
        )

    def perform_destroy(self, instance):
        item_id = instance.id
        instance.delete()
        logger.info(f"Sales order item '{item_id}' deleted successfully")
