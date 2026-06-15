from configurations.shared.created_updated_at import CreatedUpdatedAt
from django.db import models
from decimal import Decimal
from django.db.models import F, Sum
import uuid


class SalesOrder(CreatedUpdatedAt):
    class Status(models.TextChoices):
        PENDING = "PENDING", "Pending"
        CONFIRMED = "CONFIRMED", "Confirmed"
        SHIPPED = "SHIPPED", "Shipped"
        DELIVERED = "DELIVERED", "Delivered"
        CANCELLED = "CANCELLED", "Cancelled"

    PREFIX = "SO"

    user = models.ForeignKey(
        "users.CustomUser",
        on_delete=models.SET_NULL,
        null=True,
        related_name="sales_orders",
        help_text="The user who created the sales order",
    )

    order_number = models.CharField(
        max_length=255, unique=True, help_text="Unique order number"
    )

    customer = models.ForeignKey(
        "sales.Customer",
        on_delete=models.SET_NULL,
        null=True,
        related_name="sales_orders",
        help_text="The customer who placed the order",
    )

    total_amount = models.DecimalField(
        max_digits=10, decimal_places=2, help_text="Total amount for the order"
    )

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING,
        help_text="Status of the sales order",
    )

    def generate_order_number(self):
        if not self.order_number:
            unique_id = uuid.uuid4().hex[:6].upper()
            self.order_number = f"{self.PREFIX}-{unique_id}"

    def calculate_sales_order_total(self):
        return self.sales_order_items.aggregate(
            total=Sum(F("quantity") * F("unit_price"))
        ).get("total") or Decimal("0.00")

    def update_sales_order_total(self):
        total = self.calculate_sales_order_total()
        self.total_amount = total
        self.save(update_fields=["total_amount"])
        return total

    def save(self, *args, **kwargs):
        self.generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number

    class Meta:
        verbose_name = "Sales Order"
        verbose_name_plural = "Sales Orders"

        indexes = [
            models.Index(fields=["order_number"]),
            models.Index(fields=["customer_name"]),
        ]
