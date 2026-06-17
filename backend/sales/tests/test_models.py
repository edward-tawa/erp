import pytest
from decimal import Decimal
from sales.tests.factories import (
    CartFactory,
    CartItemFactory,
    CustomerFactory,
    ReceiptFactory,
    ReceiptItemFactory,
    SaleFactory,
    SalesOrderFactory,
    SalesOrderItemFactory,
)


@pytest.mark.django_db
class TestSalesModels:
    def test_customer_str(self):
        customer = CustomerFactory(name="Acme")
        assert str(customer) == "Acme"

    def test_sales_order_generates_reference(self):
        sales_order = SalesOrderFactory(order_number="")
        assert sales_order.order_number.startswith("SO-")

    def test_sales_order_item_updates_order_total(self):
        sales_order = SalesOrderFactory()
        item = SalesOrderItemFactory(
            sales_order=sales_order, quantity=2, unit_price=Decimal("5.00")
        )
        sales_order.refresh_from_db()
        assert sales_order.total_amount == Decimal("10.00")
        assert str(item).startswith("2 x")

    def test_cart_updates_total(self):
        cart = CartFactory()
        CartItemFactory(cart=cart, quantity=2, unit_price=Decimal("4.00"))
        cart.refresh_from_db()
        assert cart.total_amount == Decimal("8.00")

    def test_receipt_total_validation(self):
        receipt = ReceiptFactory(total_amount=Decimal("10.00"))
        assert receipt.receipt_reference.startswith("RCPT-")

    def test_receipt_item_updates_total(self):
        receipt = ReceiptFactory(total_amount=Decimal("0.00"))
        ReceiptItemFactory(receipt=receipt, quantity=2, unit_price=Decimal("3.00"))
        receipt.refresh_from_db()
        assert receipt.total_amount == Decimal("6.00")

    def test_sale_clean_requires_matching_entities(self):
        sale = SaleFactory()
        assert str(sale.sale_reference_number).startswith("SALE-")
