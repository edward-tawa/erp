from rest_framework import serializers
from sales.models.sale_model import Sale


class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = [
            "id",
            "sale_reference",
            "sales_order",
            "receipt",
            "user",
            "notes",
            "created_at",
            "updated_at",
        ]

        read_only_fields = [
            "id",
            "sale_reference",
            "created_at",
            "updated_at",
        ]
