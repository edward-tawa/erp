from django.db import transaction
from loguru import logger
from sales.models.cart_item_model import CartItem
from sales.services.cart_service import CartService


class CartItemService:
    @staticmethod
    @transaction.atomic
    def create_cart_item(*, cart, product, quantity, unit_price):
        cart_item = CartItem.objects.create(
            cart=cart, product=product, quantity=quantity, unit_price=unit_price
        )
        if cart_item:
            logger.info(
                f"Created cart item for product '{cart_item.product.name}' with quantity {cart_item.quantity} in cart for user '{cart.user.username}'"
            )
        else:
            logger.error(
                f"Failed to create cart item for product '{product.name}' with quantity {quantity} in cart for user '{cart.user.username}'"
            )
        CartService.calculate_cart_total(cart)
        return cart_item

    @staticmethod
    @transaction.atomic
    def create_bulk(items_data, cart):
        items = [
            CartItem(
                cart=cart,
                product=data["product"],
                quantity=data["quantity"],
                unit_price=data["unit_price"],
            )
            for data in items_data
        ]

        CartItem.objects.bulk_create(items)
        CartService.calculate_cart_total(cart)
        logger.info(f"Created bulk cart items for cart '{cart.id}'")
        return items

    @staticmethod
    @transaction.atomic
    def update_cart_item(cart_item_id, **updated_fields):
        updated_rows = CartItem.objects.filter(id=cart_item_id).update(**updated_fields)

        if updated_rows == 0:
            logger.error(f"Cart item with ID '{cart_item_id}' does not exist")
            return None

        cart_item = CartItem.objects.get(id=cart_item_id)

        CartService.calculate_cart_total(cart_item.cart)

        logger.info(f"Cart item with ID '{cart_item_id}' updated successfully")

        return cart_item

    @staticmethod
    @transaction.atomic
    def delete_cart_item(cart_item_id):
        try:
            cart_item = CartItem.objects.get(id=cart_item_id)
            cart = cart_item.cart
            cart_item.delete()
            CartService.calculate_cart_total(cart)
            logger.info(f"Cart item with ID '{cart_item_id}' deleted successfully")
            return True
        except CartItem.DoesNotExist:
            logger.error(f"Cart item with ID '{cart_item_id}' does not exist")
            return False

    @staticmethod
    def get_cart_item_by_id(cart_item_id):
        try:
            return CartItem.objects.get(id=cart_item_id)
        except CartItem.DoesNotExist:
            logger.error(f"Cart item with ID '{cart_item_id}' does not exist")
            return None

    @staticmethod
    def list_cart_items(cart_id):
        return CartItem.objects.filter(cart_id=cart_id).order_by("-created_at")
