from inventroy.models.stock_take_item_model import StockTakeItem
from django.db import transaction
from loguru import logger


class StockTakeItemService:
    @staticmethod
    @transaction.atomic
    def create_stock_take_item(*, stock_take, product, quantity):
        stock_take_item = StockTakeItem.objects.create(
            stock_take=stock_take, product=product, quantity=quantity
        )
        if stock_take_item:
            logger.info(
                f"Created stock take item for product '{stock_take_item.product.name}' with quantity {stock_take_item.quantity} in stock take '{stock_take.reference_number}'"
            )
        else:
            logger.error(
                f"Failed to create stock take item for product '{product.name}' with quantity {quantity} in stock take '{stock_take.reference_number}'"
            )
        return stock_take_item

    @staticmethod
    def list_stock_take_items(stock_take_id):
        return StockTakeItem.objects.filter(stock_take_id=stock_take_id).order_by(
            "-created_at"
        )

    @staticmethod
    @transaction.atomic
    def update_stock_take_item(stock_take_item_id, **updated_fields):
        try:
            stock_take_item = StockTakeItem.objects.get(id=stock_take_item_id)
        except StockTakeItem.DoesNotExist:
            logger.error(
                f"Stock take item with ID '{stock_take_item_id}' does not exist"
            )
            return None

        for key, value in updated_fields.items():
            setattr(stock_take_item, key, value)

        stock_take_item.save()
        logger.info(
            f"Stock take item with ID '{stock_take_item_id}' updated successfully"
        )
        return stock_take_item

    @staticmethod
    @transaction.atomic
    def delete_stock_take_item(stock_take_item_id):
        try:
            stock_take_item = StockTakeItem.objects.get(id=stock_take_item_id)
            stock_take_item.delete()
            logger.info(
                f"Stock take item with ID '{stock_take_item_id}' deleted successfully"
            )
            return True
        except StockTakeItem.DoesNotExist:
            logger.error(
                f"Stock take item with ID '{stock_take_item_id}' does not exist"
            )
            return False

    @staticmethod
    def get_stock_take_item_by_id(stock_take_item_id):
        try:
            return StockTakeItem.objects.get(id=stock_take_item_id)
        except StockTakeItem.DoesNotExist:
            logger.error(
                f"Stock take item with ID '{stock_take_item_id}' does not exist"
            )
            return None

    @staticmethod
    def get_stock_take_items_by_product(product_id):
        return StockTakeItem.objects.filter(product_id=product_id).order_by(
            "-created_at"
        )
