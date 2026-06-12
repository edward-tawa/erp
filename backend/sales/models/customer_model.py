from configurations.shared.created_updated_at import CreatedUpdatedAt
from django.db import models


class Customer(CreatedUpdatedAt):
    name = models.CharField(max_length=255, help_text="Name of the customer")
    email = models.EmailField(
        unique=True, blank=True, null=True, help_text="Email address of the customer"
    )
    phone_number = models.CharField(
        max_length=20, blank=True, null=True, help_text="Phone number of the customer"
    )
    address = models.TextField(
        blank=True, null=True, help_text="Address of the customer"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"

        indexes = [models.Index(fields=["email"])]
