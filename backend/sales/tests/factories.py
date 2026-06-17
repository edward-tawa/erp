import factory
from decimal import Decimal
from sales.models.cart_item_model import CartItem
from sales.models.cart_model import Cart
from sales.models.customer_model import Customer
from sales.models.payment_model import Payment
from sales.models.receipt_item_model import ReceiptItem
from sales.models.receipt_model import Receipt
from sales.models.sale_model import Sale
from sales.models.sales_order_item_model import SalesOrderItem
from sales.models.sales_order_model import SalesOrder
from users.tests.factories import UserFactory
from inventory.tests.factories import ProductFactory


class CustomerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Customer

    name = factory.Sequence(lambda n: f"Customer {n}")
    email = factory.Sequence(lambda n: f"customer{n}@example.com")
    phone_number = factory.Sequence(lambda n: f"+100000000{n}")
    address = factory.Faker("address")


class SalesOrderFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = SalesOrder

    user = factory.SubFactory(UserFactory)
    customer = factory.SubFactory(CustomerFactory)
    total_amount = Decimal("0.00")
    status = SalesOrder.Status.PENDING
    order_number = factory.Sequence(lambda n: f"SO-TEST-{n:05d}")


class SalesOrderItemFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = SalesOrderItem

    sales_order = factory.SubFactory(SalesOrderFactory)
    product = factory.SubFactory(ProductFactory)
    quantity = 1
    unit_price = Decimal("10.00")


class CartFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Cart

    user = factory.SubFactory(UserFactory)
    reference_number = factory.Sequence(lambda n: f"CART-TEST-{n:05d}")
    total_amount = Decimal("0.00")


class CartItemFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CartItem

    cart = factory.SubFactory(CartFactory)
    product = factory.SubFactory(ProductFactory)
    quantity = 1
    unit_price = Decimal("10.00")


class ReceiptFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Receipt

    sales_order = factory.SubFactory(SalesOrderFactory)
    user = factory.SubFactory(UserFactory)
    receipt_reference = factory.Sequence(lambda n: f"RCPT-TEST-{n:05d}")
    total_amount = Decimal("10.00")
    notes = factory.Faker("sentence")


class ReceiptItemFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ReceiptItem

    receipt = factory.SubFactory(ReceiptFactory)
    sales_order_item = factory.SubFactory(SalesOrderItemFactory)
    quantity = 1
    unit_price = Decimal("10.00")


class PaymentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Payment

    receipt = factory.SubFactory(ReceiptFactory)
    user = factory.SubFactory(UserFactory)
    payment_type = Payment.PaymentTypes.CASH
    total_amount = Decimal("10.00")
    denomination = Payment.Denomination.USD


class SaleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Sale

    user = factory.SubFactory(UserFactory)
    customer = factory.SubFactory(CustomerFactory)
    sales_order = factory.SubFactory(SalesOrderFactory)
    receipt = factory.SubFactory(ReceiptFactory)
    sale_reference_number = factory.Sequence(lambda n: f"SALE-TEST-{n:05d}")
    notes = factory.Faker("sentence")
