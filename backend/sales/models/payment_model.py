from configurations.shared.created_updated_at import CreatedUpdatedAt
from django.db import models


class Payment(CreatedUpdatedAt):
    class PaymentTypes(models.TextChoices):
        ECOCASH = "ECOCASH", "ECOCASH"
        CASH = "CASH", "CASH"
        Transfer = "TRANSFER", "TRANSFER"

    class Denomination(models.TextChoices):
        USD = "USD", "USD"
        ZWL = "ZWL", "ZWL"

    receipt = models.ForeignKey(
        "sales.Receipt",
        on_delete=models.SET_NULL,
        null=True,
        help_text="The receipt this payment is associated with",
        related_name="payments",
    )

    user = models.ForeignKey(
        "users.CustomUser",
        on_delete=models.SET_NULL,
        related_name="payments",
        help_text="The user who recorded the payment",
    )

    payment_type = models.CharField(
        max_length=20,
        choices=PaymentTypes.choices,
        help_text="The type of payment (e.g., Ecocash, Cash, Transfer)",
    )

    total_amount = models.DecimalField(
        max_digits=10, decimal_places=2, help_text="The amount paid"
    )

    denomination = models.CharField(
        max_length=10,
        choices=Denomination.choices,
        help_text="The currency denomination of the payment (e.g., USD, ZWL)",
        default=Denomination.USD,
    )

    def __str__(self):
        return f"{self.payment_type} payment of {self.total_amount} {self.denomination} for receipt {self.receipt.receipt_reference}"

    class Meta:
        verbose_name = "Payment"
        verbose_name_plural = "Payments"

        indexes = [models.Index(fields=["receipt"])]
