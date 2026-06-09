from configurations.shared.created_updated_at import CreatedUpdatedAt
from django.db import models
from decimal import Decimal
from loguru import logger
from django.core.exceptions import ValidationError


class SalesOrderItem(CreatedUpdatedAt):
    sales_order = models.ForeignKey(
        "sales.SalesOrder",
        on_delete=models.CASCADE,
        related_name="items",
        help_text="The sales order this item belongs to",
    )

    product = models.ForeignKey(
        "inventory.Product",
        on_delete=models.CASCADE,
        related_name="sales_order_items",
        help_text="The product being ordered",
    )

    quantity = models.PositiveIntegerField(help_text="Quantity of the product ordered")

    unit_price = models.DecimalField(
        max_digits=10, decimal_places=2, help_text="Unit price of the product"
    )

    def clean(self):
        if self.quantity <= 0:
            logger.info(
                f"Validation error: Quantity must be greater than zero for product '{self.product.name}' in sales order '{self.sales_order.order_number}'"
            )
            raise ValidationError("Quantity must be greater than zero")
        if self.unit_price <= Decimal("0.00"):
            logger.info(
                f"Validation error: Unit price must be greater than zero for product '{self.product.name}' in sales order '{self.sales_order.order_number}'"
            )
            raise ValidationError("Unit price must be greater than zero")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
        self.sales_order.update_sales_order_total()

    def delete(self, *args, **kwargs):
        sales_order = self.sales_order
        super().delete(*args, **kwargs)
        sales_order.update_sales_order_total()

    def __str__(self):
        return (
            f"{self.quantity} x {self.product.name} for {self.sales_order.order_number}"
        )

    class Meta:
        verbose_name = "Sales Order Item"
        verbose_name_plural = "Sales Order Items"

        indexes = [
            models.Index(fields=["sales_order"]),
            models.Index(fields=["product"]),
        ]
