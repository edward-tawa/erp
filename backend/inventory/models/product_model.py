from configurations.shared.created_updated_at import CreatedUpdatedAt
from django.db import models


class Product(CreatedUpdatedAt):
    name = models.CharField(
        max_length=255, unique=True, help_text="Name of the product"
    )

    category = models.ForeignKey(
        "inventory.Category",
        on_delete=models.SET_NULL,
        related_name="products",
        help_text="Category of the product",
        null=True,
        blank=True,
    )

    description = models.TextField(
        blank=True, null=True, help_text="Description of the product"
    )

    price = models.DecimalField(
        max_digits=10, decimal_places=2, help_text="Price of the product"
    )

    sku = models.CharField(
        max_length=100,
        unique=True,
        help_text="Stock Keeping Unit (SKU) for the product",
    )

    image = models.ImageField(
        upload_to="product_images/",
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

        indexes = [
            models.Index(fields=["name"]),
            models.Index(fields=["sku"]),
        ]
