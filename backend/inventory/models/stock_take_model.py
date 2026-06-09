from configurations.shared.created_updated_at import CreatedUpdatedAt
from django.db import models
import uuid


class StockTake(CreatedUpdatedAt):
    class Status(models.TextChoices):
        ONGOING = "ongoing", "Ongoing"
        COMPLETED = "completed", "Completed"
        CANCELED = "canceled", "Canceled"

    reference_number = models.CharField(
        max_length=100,
        unique=True,
        help_text="Unique reference number for this stock take",
    )

    notes = models.TextField(
        blank=True, null=True, help_text="Additional notes about this stock take"
    )

    taken_by = models.ForeignKey(
        "users.CustomUser",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="stock_takes",
        help_text="User who performed the stock take",
    )

    date_taken = models.DateTimeField(
        null=True,
        blank=True,
        help_text="Date and time when the stock take was completed",
    )

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.ONGOING,
        help_text="Current status of the stock take",
    )

    def __str__(self):
        return f"Stock Take {self.reference_number} - {self.created_at.date()}"

    @property
    def number_of_products_counted(self):
        """How many different products (rows/items)"""
        return self.items.count()

    @property
    def total_units_counted(self):
        """Sum of all individual quantities"""
        return self.items.aggregate(total=models.Sum("quantity"))["total"] or 0

    def generate_reference_number(self):
        """Generate a unique reference number for the stock take"""
        return f"ST-{uuid.uuid4().hex[:8].upper()}"

    def save(self, *args, **kwargs):
        if not self.reference_number:
            self.reference_number = self.generate_reference_number()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Stock Take"
        verbose_name_plural = "Stock Takes"

        indexes = [
            models.Index(fields=["reference_number"]),  # For quick lookup by reference
            models.Index(fields=["-created_at"]),  # For recent stock takes
            models.Index(fields=["taken_by", "-created_at"]),  # For user's stock takes
        ]

        ordering = ["-created_at"]  # Default ordering
