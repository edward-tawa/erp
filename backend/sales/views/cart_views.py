from rest_framework.viewsets import ModelViewSet
from sales.models.cart_model import Cart
from users.permissions.user_permissions import IsEmployee, IsManager
from sales.serializers.cart_serializer import CartSerializer
from loguru import logger


class CartViewSet(ModelViewSet):
    queryset = Cart.objects.all().order_by("-created_at")
    serializer_class = CartSerializer

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            permission_classes = [IsEmployee | IsManager]
        else:
            permission_classes = [IsManager]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        cart = serializer.save()
        logger.info(
            f"Cart '{cart.id}' created successfully for user '{cart.user.username}'"
        )

    def perform_update(self, serializer):
        cart = serializer.save()
        logger.info(
            f"Cart '{cart.id}' updated successfully for user '{cart.user.username}'"
        )

    def perform_destroy(self, instance):
        cart_id = instance.id
        instance.delete()
        logger.info(f"Cart '{cart_id}' deleted successfully")
