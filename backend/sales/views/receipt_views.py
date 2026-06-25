from rest_framework.viewsets import ModelViewSet
from sales.models.receipt_model import Receipt
from users.permissions.user_permissions import IsManager, IsAnyRole
from sales.serializers.receipt_serializer import ReceiptSerializer
from loguru import logger


class ReceiptViewSet(ModelViewSet):
    queryset = Receipt.objects.all().order_by("-created_at")
    serializer_class = ReceiptSerializer

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            permission_classes = [IsAnyRole]
        else:
            permission_classes = [IsManager]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        receipt = serializer.save()
        logger.info(
            f"Receipt '{receipt.receipt_reference}' created successfully for sales order '{receipt.sales_order.order_number}' with total amount '{receipt.total_amount}'"
        )

    def perform_update(self, serializer):
        receipt = serializer.save()
        logger.info(
            f"Receipt '{receipt.receipt_reference}' updated successfully for sales order '{receipt.sales_order.order_number}' with total amount '{receipt.total_amount}'"
        )

    def perform_destroy(self, instance):
        receipt_reference = instance.receipt_reference
        instance.delete()
        logger.info(f"Receipt '{receipt_reference}' deleted successfully")
