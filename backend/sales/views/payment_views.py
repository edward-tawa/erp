from rest_framework.viewsets import ModelViewSet
from sales.models.payment_model import Payment
from users.permissions.user_permissions import IsManager, IsAnyRole
from sales.serializers.payment_serializer import PaymentSerializer
from loguru import logger


class PaymentViewSet(ModelViewSet):
    queryset = Payment.objects.all().order_by("-created_at")
    serializer_class = PaymentSerializer

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            permission_classes = [IsAnyRole]
        else:
            permission_classes = [IsManager]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        payment = serializer.save()
        logger.info(
            f"Payment '{payment.id}' created successfully for sales order '{payment.sales_order.order_number}' with amount '{payment.amount}' and method '{payment.get_payment_method_display()}'"
        )

    def perform_update(self, serializer):
        payment = serializer.save()
        logger.info(
            f"Payment '{payment.id}' updated successfully for sales order '{payment.sales_order.order_number}' with amount '{payment.amount}' and method '{payment.get_payment_method_display()}'"
        )

    def perform_destroy(self, instance):
        payment_id = instance.id
        instance.delete()
        logger.info(f"Payment '{payment_id}' deleted successfully")
