from configurations.shared.created_updated_at import CreatedUpdatedAt
from django.db import models


class StockTakeItem(CreatedUpdatedAt):
    stock_take = models.ForeignKey(
        "inventory.StockTake",
        on_delete=models.CASCADE,
        related_name="items",
        help_text="Stock take this item belongs to",
    )

    product = models.ForeignKey(
        "inventory.Product",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="stock_take_items",
        help_text="Product associated with this stock take item",
    )

    quantity = models.IntegerField(
        help_text="Quantity of the product counted during stock take"
    )

    def __str__(self):
        return f"Stock Take Item - {self.product.name} - {self.quantity} units"

    class Meta:
        verbose_name = "Stock Take Item"
        verbose_name_plural = "Stock Take Items"

        indexes = [
            models.Index(fields=["stock_take"]),
            models.Index(fields=["product"]),
        ]
