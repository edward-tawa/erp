from rest_framework import serializers
from sales.models.customer_model import Customer


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = [
            "id",
            "name",
            "email",
            "phone_number",
            "address",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]

    def validate_email(self, value):
        if value and not serializers.EmailField().run_validation(value):
            raise serializers.ValidationError("Invalid email address")
        return value
