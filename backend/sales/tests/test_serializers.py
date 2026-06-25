import pytest
from sales.serializers.cart_item_serializer import CartItemSerializer
from sales.serializers.cart_serializer import CartSerializer
from sales.serializers.customer_serializer import CustomerSerializer
from sales.serializers.payment_serializer import PaymentSerializer
from sales.serializers.receipt_serializer import ReceiptSerializer
from sales.serializers.sale_serializer import SaleSerializer
from sales.serializers.sales_order_item_serializer import SalesOrderItemSerializer
from sales.serializers.sales_order_serializer import SalesOrderSerializer
from sales.tests.factories import (
    CartFactory,
    CustomerFactory,
    ReceiptFactory,
    SalesOrderFactory,
)
from inventory.tests.factories import ProductFactory
from users.tests.factories import UserFactory


@pytest.mark.django_db
class TestSalesSerializers:
    def test_customer_serializer_validates_email(self):
        serializer = CustomerSerializer(
            data={"name": "Acme", "email": "acme@example.com"}
        )
        assert serializer.is_valid(), serializer.errors

    def test_sales_order_serializer_requires_positive_total(self):
        customer = CustomerFactory()
        serializer = SalesOrderSerializer(
            data={"customer": customer.id, "status": "PENDING", "total_amount": "0.00"}
        )
        assert not serializer.is_valid()
        assert "total_amount" in serializer.errors

    def test_sales_order_item_serializer_requires_positive_values(self):
        sales_order = SalesOrderFactory()
        product = ProductFactory()
        serializer = SalesOrderItemSerializer(
            data={
                "sales_order": sales_order.id,
                "product": product.id,
                "quantity": 1,
                "unit_price": "10.00",
            }
        )
        assert serializer.is_valid(), serializer.errors

    def test_cart_serializer_allows_user(self):
        user = UserFactory()
        serializer = CartSerializer(data={"user": user.id})
        assert serializer.is_valid(), serializer.errors

    def test_cart_item_serializer_rejects_nonpositive_quantity(self):
        cart = CartFactory()
        product = ProductFactory()
        serializer = CartItemSerializer(
            data={
                "cart": cart.id,
                "product": product.id,
                "quantity": 0,
                "unit_price": "10.00",
            }
        )
        assert not serializer.is_valid()
        assert "quantity" in serializer.errors

    def test_payment_serializer_exposes_required_fields(self):
        receipt = ReceiptFactory()
        user = UserFactory()
        serializer = PaymentSerializer(
            data={
                "receipt": receipt.id,
                "user": user.id,
                "payment_type": "CASH",
                "total_amount": "10.00",
                "denomination": "USD",
            }
        )
        assert serializer.is_valid(), serializer.errors

    def test_receipt_serializer_matches_model(self):
        sales_order = SalesOrderFactory()
        user = UserFactory()
        serializer = ReceiptSerializer(
            data={
                "sales_order": sales_order.id,
                "user": user.id,
                "total_amount": "10.00",
            }
        )
        assert serializer.is_valid(), serializer.errors

    def test_sale_serializer_uses_sale_reference_number(self):
        sale = SaleSerializer()
        assert "sale_reference_number" in sale.get_fields()
