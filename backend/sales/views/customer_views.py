from rest_framework.viewsets import ModelViewSet
from sales.models.customer_model import Customer
from users.permissions.user_permissions import IsEmployee, IsManager
from sales.serializers.customer_serializer import CustomerSerializer
from loguru import logger


class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all().order_by("-created_at")
    serializer_class = CustomerSerializer

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            permission_classes = [IsEmployee | IsManager]
        else:
            permission_classes = [IsManager]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        customer = serializer.save()
        logger.info(
            f"Customer '{customer.name}' created successfully with email '{customer.email}' and phone '{customer.phone_number}'"
        )

    def perform_update(self, serializer):
        customer = serializer.save()
        logger.info(
            f"Customer '{customer.name}' updated successfully with email '{customer.email}' and phone '{customer.phone_number}'"
        )

    def perform_destroy(self, instance):
        customer_name = instance.name
        instance.delete()
        logger.info(f"Customer '{customer_name}' deleted successfully")
