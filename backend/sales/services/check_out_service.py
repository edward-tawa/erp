from django.db import transaction
from sales.models.cart_model import Cart
from sales.services.receipt_item_service import ReceiptItemService
from sales.services.sale_service import SaleService
from sales.services.sales_order_service import SalesOrderService
from sales.services.sales_order_item_service import SalesOrderItemService
from sales.services.receipt_service import ReceiptService


class CheckOutService:
    @staticmethod
    @transaction.atomic
    def checkout_cart(cart: Cart, user, customer, notes=None):
        # create sales order
        sales_order = SalesOrderService.create_sales_order(
            user,
            customer,
        )

        # create sales order items from cart items
        cart_items = cart.items.all()
        for item in cart_items:
            SalesOrderItemService.create_sales_order_item(
                sales_order=sales_order,
                product=item.product,
                quantity=item.quantity,
                unit_price=item.unit_price,
            )

        # create receipt for the sales order
        receipt = ReceiptService.create_receipt(
            user=user, sales_order=sales_order, notes=notes
        )

        # create receipt items from sales order items
        ReceiptItemService.create_receipt_items(
            receipt=receipt, sales_order=sales_order
        )

        # create a sale associated with the receipt
        sale = SaleService.create_sale(
            sales_order=sales_order, user=user, receipt=receipt, notes=notes
        )

        cart.items.all().delete()

        return {"sales_order": sales_order, "receipt": receipt, "sale": sale}
