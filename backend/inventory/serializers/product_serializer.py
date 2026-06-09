from rest_framework import serializers
from inventroy.models.product_model import Product
from inventroy.models.category_model import Category


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), required=False, allow_null=True
    )

    class Meta:
        model = Product
        fields = [
            "name",
            "category",
            "description",
            "price",
            "sku",
            "image",
            "created_at",
            "updated_at",
        ]

        extra_kwargs = {
            "name": {"required": True},
            "price": {"required": True},
            "sku": {"required": True},
            "created_at": {"read_only": True},
            "updated_at": {"read_only": True},
        }
