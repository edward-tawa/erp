from rest_framework import serializers
from inventroy.models.stock_take_item_model import StockTakeItem


class StockTakeItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockTakeItem
        fields = [
            "id",
            "stock_take",
            "product",
            "quantity",
            "created_at",
            "updated_at",
        ]

        extra_kwargs = {
            "stock_take": {"required": True},
            "product": {"required": True},
            "quantity": {"required": True},
            "created_at": {"read_only": True},
            "updated_at": {"read_only": True},
        }
