from rest_framework import serializers
from inventroy.models.stock_take_model import StockTake


class StockTakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockTake
        fields = [
            "id",
            "reference_number",
            "product",
            "taken_by",
            "date_taken",
            "status",
            "created_at",
            "updated_at",
        ]

        extra_kwargs = {
            "reference_number": {"read_only": True},
            "product": {"required": True},
            "taken_by": {"required": True},
            "date_taken": {"required": True},
            "created_at": {"read_only": True},
            "updated_at": {"read_only": True},
        }
