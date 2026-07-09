from rest_framework import serializers
from sales.models.sale_model import Sale
from sales.models.sales_order_model import SalesOrder
from sales.models.receipt_model import Receipt


class SaleSerializer(serializers.ModelSerializer):
    sales_order = serializers.PrimaryKeyRelatedField(queryset=SalesOrder.objects.all())
    receipt = serializers.PrimaryKeyRelatedField(queryset=Receipt.objects.all())
    notes = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = Sale
        fields = [
            "id",
            "sale_reference_number",
            "sales_order",
            "receipt",
            "user",
            "notes",
            "created_at",
            "updated_at",
        ]

        read_only_fields = [
            "id",
            "sale_reference_number",
            "created_at",
            "updated_at",
        ]

    def validate(self, attrs):
        sales_order = attrs.get("sales_order")
        receipt = attrs.get("receipt")

        # Safety checks (important if partial updates happen)
        if not sales_order or not receipt:
            return attrs

        # receipt must belong to same order (if applicable in your schema)
        if hasattr(receipt, "sales_order") and receipt.sales_order != sales_order:
            raise serializers.ValidationError(
                {"receipt": "Receipt does not belong to this sales order."}
            )

        # totals must match (strict case)
        if receipt.total_amount != sales_order.total_amount:
            raise serializers.ValidationError(
                {"receipt": "Receipt total must match sales order total."}
            )

        return attrs
