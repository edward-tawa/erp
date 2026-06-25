from rest_framework import serializers
from sales.models.receipt_model import Receipt


class ReceiptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receipt
        fields = [
            "id",
            "receipt_reference",
            "sales_order",
            "user",
            "total_amount",
            "notes",
            "created_at",
            "updated_at",
        ]
        read_only_fields = [
            "id",
            "receipt_reference",
            "total_amount",
            "created_at",
            "updated_at",
        ]

        def validate_total_amount(self, value):
            if value <= 0:
                raise serializers.ValidationError(
                    "Total amount cannot be zero or negative"
                )
            return value
