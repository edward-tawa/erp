from configurations.shared.created_updated_at import CreatedUpdatedAt
from django.db import models


class StockMovement(CreatedUpdatedAt):
    class MovementType(models.TextChoices):
        PURCHASE = "purchase", "Purchase"
        SALE = "sale", "Sale"
        SALES_RETURN = "sales_return", "Sales Return"
        PURCHASE_RETURN = "purchase_return", "Purchase Return"
        ADJUSTMENT = "adjustment", "Adjustment"

    product = models.ForeignKey(
        "inventory.Product",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="stock_movements",
        help_text="Product associated with this stock movement",
    )

    quantity = models.IntegerField(help_text="Quantity of the product moved")

    movement_type = models.CharField(
        max_length=20,
        choices=MovementType.choices,
        help_text="Type of stock movement",
    )

    def __str__(self):
        return f"{self.get_movement_type_display()} - {self.product.name} - {self.quantity} units"
