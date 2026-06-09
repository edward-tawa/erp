from configurations.shared.created_updated_at import CreatedUpdatedAt
from django.db import models


class ProductStock(CreatedUpdatedAt):
    product = models.OneToOneField(
        "inventory.Product",
        on_delete=models.CASCADE,
        related_name="stock",
        help_text="Product associated with this stock entry",
    )

    quantity = models.PositiveIntegerField(help_text="Quantity of the product in stock")

    min_stock_level = models.PositiveIntegerField(
        help_text="Minimum stock level to trigger restocking",
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.product.name} - {self.quantity} units"

    class Meta:
        verbose_name = "Stock"
        verbose_name_plural = "Stocks"

        indexes = [
            models.Index(fields=["product"]),
            models.Index(fields=["min_stock_level"]),
        ]
