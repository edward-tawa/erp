from rest_framework import serializers
from inventroy.models.product_model import Product
from inventroy.models.product_stock_model import ProductStock


class ProductStockSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(), required=True
    )

    class Meta:
        model = ProductStock
        fields = [
            "product",
            "quantity",
            "min_stock_level",
            "created_at",
            "updated_at",
        ]

        extra_kwargs = {
            "quantity": {"required": True},
            "created_at": {"read_only": True},
            "updated_at": {"read_only": True},
        }
