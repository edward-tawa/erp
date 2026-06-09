from configurations.shared.created_updated_at import CreatedUpdatedAt
from django.db import models


class Category(CreatedUpdatedAt):
    name = models.CharField(
        max_length=255, unique=True, help_text="Name of the category"
    )

    description = models.TextField(
        blank=True, null=True, help_text="Description of the category"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

        indexes = [models.Index(fields=["name"])]
