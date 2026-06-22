from django.core.exceptions import ValidationError
from configurations.shared.created_updated_at import CreatedUpdatedAt
from django.db import models
import uuid


class Sale(CreatedUpdatedAt):
    PREFIX = "SALE"

    user = models.ForeignKey(
        "users.CustomUser",
        on_delete=models.SET_NULL,
        null=True,
        related_name="sales",
        help_text="The user who created the sale",
    )

    customer = models.ForeignKey(
        "sales.Customer",
        on_delete=models.SET_NULL,
        null=True,
        related_name="sales",
        help_text="The customer associated with the sale",
    )

    sales_order = models.OneToOneField(
        "sales.SalesOrder",
        on_delete=models.SET_NULL,
        null=True,
        related_name="sale",
        help_text="The sales order associated with the sale",
    )

    receipt = models.OneToOneField(
        "sales.Receipt",
        on_delete=models.SET_NULL,
        null=True,
        related_name="sale",
        help_text="The receipt associated with the sale",
    )

    sale_reference_number = models.CharField(
        max_length=255, unique=True, help_text="Unique reference number for the sale"
    )

    notes = models.TextField(
        blank=True, null=True, help_text="Additional notes for the sale"
    )

    @property
    def total_amount(self):
        if self.sales_order:
            return self.sales_order.total_amount
        return 0.00

    # not being used now
    def clean(self):
        if not self.sales_order or not self.receipt:
            return  # don't validate incomplete object

        if self.sales_order.total_amount != self.receipt.total_amount:
            raise ValidationError("Sales order and receipt totals do not match.")

    def generate_sale_reference_number(self):
        if not self.sale_reference_number:
            unique_id = uuid.uuid4().hex[:8].upper()
            self.sale_reference_number = f"{self.PREFIX}-{unique_id}"

    def save(self, *args, **kwargs):
        self.generate_sale_reference_number()
        super().save(*args, **kwargs)

    def __str__(self):
        customer_name = self.customer.name if self.customer else "Unknown Customer"
        return f"{self.sale_reference_number} - {customer_name}"

    class Meta:
        verbose_name = "Sale"
        verbose_name_plural = "Sales"

        indexes = [
            models.Index(fields=["customer"]),
            models.Index(fields=["sale_reference_number"]),
        ]
