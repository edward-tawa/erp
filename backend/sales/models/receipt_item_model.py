from configurations.shared.created_updated_at import CreatedUpdatedAt
from django.db import models
from loguru import logger
from django.core.exceptions import ValidationError


class ReceiptItem(CreatedUpdatedAt):
    receipt = models.ForeignKey(
        "sales.Receipt",
        on_delete=models.CASCADE,
        related_name="items",
        help_text="The receipt this item belongs to",
    )

    sales_order_item = models.ForeignKey(
        "sales.SalesOrderItem",
        on_delete=models.CASCADE,
        related_name="receipt_items",
        help_text="The sales order item being included in the receipt",
    )

    quantity = models.PositiveIntegerField(
        help_text="Quantity of the product in the receipt"
    )

    unit_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text="Unit price of the product in the receipt",
    )

    def clean(self):
        if self.quantity <= 0:
            logger.info(
                f"Validation error: Quantity must be greater than zero for product '{self.sales_order_item.product.name}' in receipt '{self.receipt.receipt_reference}'"
            )
            raise ValidationError("Quantity must be greater than zero")
        if self.unit_price <= 0:
            logger.info(
                f"Validation error: Unit price must be greater than zero for product '{self.sales_order_item.product.name}' in receipt '{self.receipt.receipt_reference}'"
            )
            raise ValidationError("Unit price must be greater than zero")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
        self.receipt.update_total_amount()

    def delete(self, *args, **kwargs):
        receipt = self.receipt
        super().delete(*args, **kwargs)
        logger.info(
            f"Deleted receipt item for product '{self.sales_order_item.product.name}' from receipt '{receipt.receipt_reference}'"
        )
        receipt.update_total_amount()
