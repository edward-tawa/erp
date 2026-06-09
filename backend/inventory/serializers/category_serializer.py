from rest_framework import serializers
from inventroy.models.category_model import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "description", "created_at", "updated_at"]

        extra_kwargs = {
            "name": {"required": True},
            "description": {"required": False, "allow_blank": True},
            "created_at": {"read_only": True},
            "updated_at": {"read_only": True},
        }
