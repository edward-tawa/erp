from django.db import transaction
from loguru import logger
from sales.models.receipt_model import Receipt
from decimal import Decimal
from django.db.models import F, Sum


class ReceiptService:
    @staticmethod
    @transaction.atomic
    def create_receipt(*, sales_order, user, notes=None):
        logger.info(f"Creating receipt for sales order '{sales_order.order_number}'")
        try:
            receipt = Receipt.objects.create(
                sales_order=sales_order,
                user=user,
                notes=notes,
            )
            logger.info(
                f"Receipt '{receipt.receipt_reference}' created for sales order '{sales_order.order_number}'"
            )
        except Exception as e:
            logger.error(f"Error occurred while creating receipt: {e}")
            raise

        return receipt

    @staticmethod
    def update_receipt(receipt_id, **updated_fields):
        Receipt.objects.filter(id=receipt_id).update(**updated_fields)
        logger.info(f"Receipt with ID '{receipt_id}' updated successfully")
        return receipt_id

    @staticmethod
    @transaction.atomic
    def delete_receipt(receipt_id):
        try:
            receipt = Receipt.objects.get(id=receipt_id)
            receipt.delete()
            logger.info(f"Receipt with ID '{receipt_id}' deleted successfully")
            return True
        except Receipt.DoesNotExist:
            logger.error(f"Receipt with ID '{receipt_id}' does not exist")
            return False

    @staticmethod
    def get_receipt_by_id(receipt_id):
        try:
            return Receipt.objects.get(id=receipt_id)
        except Receipt.DoesNotExist:
            logger.error(f"Receipt with ID '{receipt_id}' does not exist")
            return None

    @staticmethod
    def calculate_receipt_total_amount(receipt_id):
        try:
            receipt = Receipt.objects.get(id=receipt_id)
            total = receipt.items.aggregate(
                total=Sum(F("quantity") * F("unit_price"))
            ).get("total", Decimal("0.00")) or Decimal("0.00")
            return total
        except Receipt.DoesNotExist:
            logger.error(f"Receipt with ID '{receipt_id}' does not exist")
            return Decimal("0.00")

    @staticmethod
    @transaction.atomic
    def update_receipt_total_amount(receipt_id):
        try:
            receipt = Receipt.objects.get(id=receipt_id)
            receipt.total_amount = ReceiptService.calculate_receipt_total_amount(
                receipt_id
            )
            receipt.save(update_fields=["total_amount"])
            logger.info(
                f"Receipt with ID '{receipt_id}' total amount updated to {receipt.total_amount}"
            )
        except Receipt.DoesNotExist:
            logger.error(f"Receipt with ID '{receipt_id}' does not exist")
