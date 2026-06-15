from rest_framework.viewsets import ModelViewSet
from sales.models.receipt_item_model import ReceiptItem
from sales.serializers.receipt_item_serializer import ReceiptItemSerializer
from users.permissions.user_permissions import IsEmployee, IsManager
from loguru import logger


class ReceiptItemViewSet(ModelViewSet):
    queryset = ReceiptItem.objects.all().order_by("-created_at")
    serializer_class = ReceiptItemSerializer

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            permission_classes = [IsEmployee | IsManager]
        else:
            permission_classes = [IsManager]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        receipt_item = serializer.save()
        logger.info(
            f"Receipt item '{receipt_item.id}' created successfully for receipt '{receipt_item.receipt.receipt_reference}' with product '{receipt_item.product.name}' and quantity '{receipt_item.quantity}'"
        )

    def perform_update(self, serializer):
        receipt_item = serializer.save()
        logger.info(
            f"Receipt item '{receipt_item.id}' updated successfully for receipt '{receipt_item.receipt.receipt_reference}' with product '{receipt_item.product.name}' and quantity '{receipt_item.quantity}'"
        )

    def perform_destroy(self, instance):
        item_id = instance.id
        instance.delete()
        logger.info(f"Receipt item '{item_id}' deleted successfully")
