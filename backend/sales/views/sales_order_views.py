from rest_framework.viewsets import ModelViewSet
from sales.models.sales_order_model import SalesOrder
from users.permissions.user_permissions import IsEmployee, IsManager
from sales.serializers.sales_order_serializer import SalesOrderSerializer
from loguru import logger


class SalesOrderViewSet(ModelViewSet):
    queryset = SalesOrder.objects.all().order_by("-created_at")
    serializer_class = SalesOrderSerializer

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            permission_classes = [IsEmployee | IsManager]
        else:
            permission_classes = [IsManager]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        sales_order = serializer.save()
        logger.info(
            f"Sales order '{sales_order.order_number}' created successfully with status '{sales_order.get_status_display()}'"
        )

    def perform_update(self, serializer):
        sales_order = serializer.save()
        logger.info(
            f"Sales order '{sales_order.order_number}' updated successfully with status '{sales_order.get_status_display()}'"
        )

    def perform_destroy(self, instance):
        order_number = instance.order_number
        instance.delete()
        logger.info(f"Sales order '{order_number}' deleted successfully")
