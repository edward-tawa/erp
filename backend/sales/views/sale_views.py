from rest_framework.viewsets import ModelViewSet
from users.permissions.user_permissions import IsEmployee, IsManager
from sales.models.sale_model import Sale
from sales.serializers.sale_serializer import SaleSerializer
from loguru import logger


class SaleViewSet(ModelViewSet):
    queryset = Sale.objects.all().order_by("-created_at")
    serializer_class = SaleSerializer

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            permission_classes = [IsEmployee]
        else:
            permission_classes = [IsManager]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        sale = serializer.save()
        logger.info(
            f"Sale '{sale.sale_reference}' created successfully for sales order '{sale.sales_order.order_number}'"
        )

    def perform_update(self, serializer):
        sale = serializer.save()
        logger.info(
            f"Sale '{sale.sale_reference}' updated successfully for sales order '{sale.sales_order.order_number}'"
        )

    def perform_destroy(self, instance):
        sale_reference = instance.sale_reference
        instance.delete()
        logger.info(f"Sale '{sale_reference}' deleted successfully")
