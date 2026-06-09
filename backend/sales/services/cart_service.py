from django.db import transaction
from loguru import logger
from sales.models.cart_model import Cart
from django.db.models import F, Sum
from decimal import Decimal


class CartService:
    @staticmethod
    @transaction.atomic
    def create_cart(*, user):
        cart = Cart.objects.create(user=user)
        if cart:
            logger.info(f"Created cart for user '{cart.user.username}'")
        else:
            logger.error(f"Failed to create cart for user '{user.username}'")
        return cart

    @staticmethod
    @transaction.atomic
    def update_cart(cart_id, **updated_fields):
        Cart.objects.filter(id=cart_id).update(**updated_fields)
        logger.info(f"Cart with ID '{cart_id}' updated successfully")
        return cart_id

    @staticmethod
    @transaction.atomic
    def delete_cart(cart_id):
        try:
            cart = Cart.objects.get(id=cart_id)
            cart.delete()
            logger.info(f"Cart with ID '{cart_id}' deleted successfully")
            return True
        except Cart.DoesNotExist:
            logger.error(f"Cart with ID '{cart_id}' does not exist")
            return False

    @staticmethod
    def get_cart_by_id(cart_id):
        try:
            return Cart.objects.get(id=cart_id)
        except Cart.DoesNotExist:
            logger.error(f"Cart with ID '{cart_id}' does not exist")
            return None

    @staticmethod
    def calculate_cart_total(cart):
        total = cart.cart_items.aggregate(
            total=Sum(F("quantity") * F("unit_price"))
        ).get("total", Decimal("0.00")) or Decimal("0.00")
        cart.total_amount = total
        cart.save(update_fields=["total_amount"])
        return total
