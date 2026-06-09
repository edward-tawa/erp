from inventroy.models.stock_movement_model import StockMovement
from django.db import transaction
from loguru import logger


class StockMovementService:
    @staticmethod
    @transaction.atomic
    def create_stock_movement(*, product, quantity, movement_type):
        stock_movement = StockMovement.objects.create(
            product=product, quantity=quantity, movement_type=movement_type
        )
        if stock_movement:
            logger.info(
                f"Created stock movement for product '{stock_movement.product.name}' with quantity {stock_movement.quantity} and type '{stock_movement.get_movement_type_display()}'"
            )
        else:
            logger.error(
                f"Failed to create stock movement for product '{product.name}' with quantity {quantity} and type '{movement_type}'"
            )
        return stock_movement

    @staticmethod
    def list_stock_movements():
        return StockMovement.objects.all().order_by("-created_at")
