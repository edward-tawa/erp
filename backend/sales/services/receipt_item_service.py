from django.db import transaction
from loguru import logger
from sales.models.receipt_item_model import ReceiptItem
from sales.services.receipt_service import ReceiptService


class ReceiptItemService:
    @staticmethod
    @transaction.atomic
    def create_receipt_item(*, receipt, sales_order_item, quantity, unit_price):
        receipt_item = ReceiptItem.objects.create(
            receipt=receipt,
            sales_order_item=sales_order_item,
            quantity=quantity,
            unit_price=unit_price,
        )
        if receipt_item:
            ReceiptService.update_total_amount(receipt_item.receipt.id)
            logger.info(
                f"Created receipt item for product '{receipt_item.sales_order_item.product.name}' with quantity {receipt_item.quantity} and unit price {receipt_item.unit_price} in receipt '{receipt.receipt_reference}'"
            )
        else:
            logger.error(
                f"Failed to create receipt item for product '{sales_order_item.product.name}' with quantity {quantity} and unit price {unit_price} in receipt '{receipt.receipt_reference}'"
            )
        return receipt_item

    def update_receipt_item(receipt_item_id, **updated_fields):
        try:
            receipt_item_row = ReceiptItem.objects.filter(id=receipt_item_id).update(
                **updated_fields
            )
            if receipt_item_row:
                receipt_item = ReceiptItem.objects.get(id=receipt_item_id)
                ReceiptService.calculate_receipt_total_amount(receipt_item.receipt.id)
                ReceiptService.update_receipt_total_amount(receipt_item.receipt.id)
                logger.info(
                    f"Updated receipt item with ID '{receipt_item_id}' successfully"
                )
                return receipt_item
            else:
                logger.error(
                    f"Failed to update receipt item with ID '{receipt_item_id}'"
                )
                return None
        except ReceiptItem.DoesNotExist:
            logger.error(f"Receipt item with ID '{receipt_item_id}' does not exist")
            return None

    @staticmethod
    @transaction.atomic
    def delete_receipt_item(receipt_item_id):
        try:
            receipt_item = ReceiptItem.objects.get(id=receipt_item_id)
            receipt = receipt_item.receipt
            receipt_item.delete()
            logger.info(
                f"Receipt item with ID '{receipt_item_id}' deleted successfully"
            )
            ReceiptService.calculate_receipt_total_amount(receipt.id)
            ReceiptService.update_receipt_total_amount(receipt.id)
            return True
        except ReceiptItem.DoesNotExist:
            logger.error(f"Receipt item with ID '{receipt_item_id}' does not exist")
            return False

    @staticmethod
    def get_receipt_item_by_id(receipt_item_id):
        try:
            return ReceiptItem.objects.get(id=receipt_item_id)
        except ReceiptItem.DoesNotExist:
            logger.error(f"Receipt item with ID '{receipt_item_id}' does not exist")
            return None

    @staticmethod
    @transaction.atomic
    def bulk_create_receipt_items(items_data, receipt):
        items = [
            ReceiptItem(
                receipt=receipt,
                sales_order_item=data["sales_order_item"],
                quantity=data["quantity"],
                unit_price=data["unit_price"],
            )
            for data in items_data
        ]

        ReceiptItem.objects.bulk_create(items)

        ReceiptService.calculate_receipt_total_amount(receipt.id)
        ReceiptService.update_receipt_total_amount(receipt.id)
        return items
