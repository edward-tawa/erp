from rest_framework.viewsets import ModelViewSet
from sales.models.cart_item_model import CartItem
from sales.serializers.cart_item_serializer import CartItemSerializer
from users.permissions.user_permissions import IsManager, IsAnyRole
from loguru import logger


class CartItemViewSet(ModelViewSet):
    queryset = CartItem.objects.all().order_by("-created_at")
    serializer_class = CartItemSerializer

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            permission_classes = [IsAnyRole]
        else:
            permission_classes = [IsManager]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        cart_item = serializer.save()
        logger.info(
            f"Cart item '{cart_item.id}' created successfully for cart '{cart_item.cart.id}' with product '{cart_item.product.name}' and quantity '{cart_item.quantity}'"
        )

    def perform_update(self, serializer):
        cart_item = serializer.save()
        logger.info(
            f"Cart item '{cart_item.id}' updated successfully for cart '{cart_item.cart.id}' with product '{cart_item.product.name}' and quantity '{cart_item.quantity}'"
        )

    def perform_destroy(self, instance):
        item_id = instance.id
        instance.delete()
        logger.info(f"Cart item '{item_id}' deleted successfully")
