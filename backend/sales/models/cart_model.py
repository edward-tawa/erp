from configurations.shared.created_updated_at import CreatedUpdatedAt
from django.db import models
from decimal import Decimal
from django.db.models import F, Sum
import uuid


class Cart(CreatedUpdatedAt):
    PREFIX = "CART"

    user = models.OneToOneField(
        "auth.User", on_delete=models.CASCADE, related_name="cart"
    )

    reference_number = models.CharField(max_length=50, unique=True, editable=False)

    total_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=Decimal("0.00"),
        help_text="Total amount for the cart",
    )

    def generate_reference_number(self):
        if not self.reference_number:
            self.reference_number = f"{self.PREFIX}-{uuid.uuid4().hex[:6].upper()}"

    def update_cart_total(self):
        total = self.cart_items.aggregate(
            total=Sum(F("quantity") * F("unit_price"))
        ).get("total", Decimal("0.00")) or Decimal("0.00")
        self.total_amount = total
        self.save(update_fields=["total_amount"])

    def save(self, *args, **kwargs):
        self.generate_reference_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Cart for {self.user.username} ({self.reference_number})"

    class Meta:
        verbose_name = "Cart"
        verbose_name_plural = "Carts"

        indexes = [models.Index(fields=["reference_number"])]
