from rest_framework import serializers
from sales.models.cart_model import Cart
from sales.models.customer_model import Customer


class CheckoutSerializer(serializers.Serializer):
    cart = serializers.PrimaryKeyRelatedField(queryset=Cart.objects.all())
    customer = serializers.PrimaryKeyRelatedField(queryset=Customer.objects.all())
    notes = serializers.CharField(required=False, allow_blank=True, allow_null=True)
