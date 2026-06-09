from inventroy.models.stock_take_model import StockTake
from django.db import transaction
from loguru import logger


class StockTakeService:
    @staticmethod
    @transaction.atomic
    def create_stock_take(*, reference_number, quantity, status=None, notes=None):
        stock_take = StockTake.objects.create(
            reference_number=reference_number,
            quantity=quantity,
            status=status or StockTake.Status.ONGOING,
            notes=notes,
        )
        if stock_take:
            logger.info(
                f"Created stock take with reference number '{stock_take.reference_number}' and quantity {stock_take.quantity}"
            )
        else:
            logger.error(
                f"Failed to create stock take with reference number '{reference_number}' and quantity {quantity}"
            )
        return stock_take

    @staticmethod
    def list_stock_takes():
        return StockTake.objects.all().order_by("-created_at")

    @staticmethod
    @transaction.atomic
    def update_stock_take(stock_take_id, **updated_fields):
        try:
            stock_take = StockTake.objects.get(id=stock_take_id)
        except StockTake.DoesNotExist:
            logger.error(f"Stock take with ID '{stock_take_id}' does not exist")
            return None

        for key, value in updated_fields.items():
            setattr(stock_take, key, value)

        stock_take.save()
        logger.info(f"Stock take with ID '{stock_take_id}' updated successfully")
        return stock_take

    @staticmethod
    @transaction.atomic
    def delete_stock_take(stock_take_id):
        try:
            stock_take = StockTake.objects.get(id=stock_take_id)
            stock_take.delete()
            logger.info(f"Stock take with ID '{stock_take_id}' deleted successfully")
            return True
        except StockTake.DoesNotExist:
            logger.error(f"Stock take with ID '{stock_take_id}' does not exist")
            return False

    @staticmethod
    def get_stock_take_by_id(stock_take_id):
        try:
            return StockTake.objects.get(id=stock_take_id)
        except StockTake.DoesNotExist:
            logger.error(f"Stock take with ID '{stock_take_id}' does not exist")
            return None

    @staticmethod
    def get_stock_take_by_reference(reference_number):
        try:
            return StockTake.objects.get(reference_number=reference_number)
        except StockTake.DoesNotExist:
            logger.error(
                f"Stock take with reference number '{reference_number}' does not exist"
            )
            return None
