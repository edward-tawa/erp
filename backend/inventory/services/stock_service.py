from inventory.models.product_stock_model import ProductStock
from django.db import transaction
from loguru import logger


class StockService:
    @staticmethod
    @transaction.atomic
    def create_stock(*, product, quantity, min_stock_level=None):
        product_stock = ProductStock.objects.create(
            product=product, quantity=quantity, min_stock_level=min_stock_level
        )
        if product_stock:
            logger.info(
                f"Created stock entry for product '{product_stock.product.name}' with quantity {product_stock.quantity}"
            )
        else:
            logger.error(f"Failed to create stock entry for product '{product.name}'")
        return product_stock

    @staticmethod
    @transaction.atomic
    def update_stock(stock_id, **updated_fields):
        try:
            product_stock = ProductStock.objects.get(id=stock_id)
        except ProductStock.DoesNotExist:
            logger.error(f"Stock with ID '{stock_id}' does not exist")
            return None

        for key, value in updated_fields.items():
            setattr(product_stock, key, value)

        product_stock.save()
        logger.info(f"Stock with ID '{stock_id}' updated successfully")
        return product_stock

    @staticmethod
    @transaction.atomic
    def delete_stock(product_stock_id):
        try:
            product_stock = ProductStock.objects.get(id=product_stock_id)
            product_stock.delete()
            logger.info(f"Stock with ID '{product_stock_id}' deleted successfully")
            return True
        except ProductStock.DoesNotExist:
            logger.error(f"Stock with ID '{product_stock_id}' does not exist")
            return False

    @staticmethod
    def get_stock_by_id(product_stock_id):
        try:
            return ProductStock.objects.get(id=product_stock_id)
        except ProductStock.DoesNotExist:
            logger.error(f"Stock with ID '{product_stock_id}' does not exist")
            return None

    @staticmethod
    def list_product_stocks():
        return ProductStock.objects.all().order_by("-id")

    @staticmethod
    def adjust_product_stock(product_id, quantity_change):
        try:
            stock = ProductStock.objects.select_for_update().get(product_id=product_id)
            new_quantity = stock.quantity + quantity_change

            if new_quantity < 0:
                logger.warning(
                    f"Attempting to reduce stock for product ID '{product_id}' below zero. "
                    f"Current quantity: {stock.quantity}, attempted change: {quantity_change}"
                )
                return None

            stock.quantity = new_quantity
            stock.save()

            logger.info(
                f"Adjusted stock for product ID '{product_id}' by {quantity_change}."
                f"New quantity: {stock.quantity}"
            )
            return stock

        except ProductStock.DoesNotExist:
            logger.error(f"Stock for product ID '{product_id}' does not exist")
            return None
