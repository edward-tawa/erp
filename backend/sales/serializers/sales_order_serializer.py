from rest_framework import serializers
from sales.models.sales_order_model import SalesOrder
from sales.models.customer_model import Customer


class SalesOrderSerializer(serializers.ModelSerializer):
    customer = serializers.PrimaryKeyRelatedField(
        queryset=Customer.objects.all(),
        help_text="ID of the customer placing the order",
    )

    total_amount = serializers.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text="Total amount for the order",
    )

    class Meta:
        model = SalesOrder
        fields = [
            "id",
            "order_number",
            "customer",
            "status",
            "total_amount",
            "created_at",
            "updated_at",
        ]
        read_only_fields = [
            "id",
            "order_number",
            "total_amount",
            "created_at",
            "updated_at",
        ]

    def validate_total_amount(self, value):
        if value <= 0:
            raise serializers.ValidationError("Total amount cannot be zero or negative")
