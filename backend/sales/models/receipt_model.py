from configurations.shared.created_updated_at import CreatedUpdatedAt
from django.db import models
from django.core.exceptions import ValidationError
from django.db.models import F, Sum
from decimal import Decimal
import uuid


class Receipt(CreatedUpdatedAt):
    PREFIX = "RCPT"
    sales_order = models.ForeignKey(
        "sales.SalesOrder",
        on_delete=models.SET_NULL,
        related_name="receipt",
        help_text="receipt for the sales order",
    )

    user = models.ForeignKey(
        "users.CustomUser",
        on_delete=models.SET_NULL,
        related_name="receipts",
        help_text="The user who created the receipt",
    )

    receipt_reference = models.CharField(
        max_length=255,
        unique=True,
        help_text="Unique reference for the receipt, typically generated based on the sales order",
    )

    total_amount = models.DecimalField(
        max_digits=10, decimal_places=2, help_text="Total amount for the receipt"
    )

    notes = models.TextField(
        blank=True, null=True, help_text="Additional notes for the receipt"
    )

    def generate_receipt_reference(self):
        return f"{self.PREFIX}-{uuid.uuid4().hex[:8].upper()}"

    def calculate_total_amount(self):
        return self.items.aggregate(total=Sum(F("quantity") * F("unit_price"))).get(
            "total", Decimal("0.00")
        ) or Decimal("0.00")

    def update_total_amount(self):
        total = self.calculate_total_amount()
        self.total_amount = total
        self.save(update_fields=["total_amount"])
        return total

    def clean(self):
        if self.total_amount < 0:
            raise ValidationError("Total amount cannot be negative")

    def save(self, *args, **kwargs):
        self.full_clean()
        if not self.receipt_reference:
            self.receipt_reference = self.generate_receipt_reference()
        if self.total_amount is None:
            self.total_amount = self.calculate_total_amount()
        super().save(*args, **kwargs)
