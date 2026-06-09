from rest_framework import serializers
from inventroy.models.stock_movement_model import StockMovement


class StockMovementSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockMovement
        fields = [
            "id",
            "product",
            "quantity",
            "movement_type",
            "created_at",
            "updated_at",
        ]

        extra_kwargs = {
            "product": {"required": True},
            "quantity": {"required": True},
            "movement_type": {"required": True},
            "created_at": {"read_only": True},
            "updated_at": {"read_only": True},
        }
