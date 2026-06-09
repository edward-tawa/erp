from django.db import transaction
from loguru import logger
from sales.models.sales_order_item_model import SalesOrderItem
from sales.models.sales_order_model import SalesOrder
from django.db.models import F, Sum
from decimal import Decimal


class SalesOrderService:
    @staticmethod
    def update_sales_order_total(sales_order):
        total = (
            SalesOrderItem.objects.filter(sales_order=sales_order)
            .aggregate(total=Sum(F("quantity") * F("unit_price")))
            .get("total")
        ) or Decimal("0.00")

        type(sales_order).objects.filter(id=sales_order.id).update(total_amount=total)

        return total

    @staticmethod
    @transaction.atomic
    def create_sales_order(*, customer_name=None, order_number, status="pending"):
        sales_order = SalesOrder.objects.create(
            customer_name=customer_name, order_number=order_number, status=status
        )
        if sales_order:
            logger.info(
                f"Created sales order '{sales_order.order_number}' for customer '{sales_order.customer_name}' with status '{sales_order.get_status_display()}'"
            )
        else:
            logger.error(
                f"Failed to create sales order '{order_number}' for customer '{customer_name}' with status '{status}'"
            )
        return sales_order

    @staticmethod
    @transaction.atomic
    def update_sales_order(sales_order_id, **updated_fields):
        updated_rows = SalesOrder.objects.filter(id=sales_order_id).update(
            **updated_fields
        )

        if updated_rows == 0:
            logger.error(f"Sales order with ID '{sales_order_id}' does not exist")
            return None

        logger.info(f"Sales order with ID '{sales_order_id}' updated successfully")
        return SalesOrder.objects.get(id=sales_order_id)

    @staticmethod
    @transaction.atomic
    def delete_sales_order(sales_order_id):
        try:
            sales_order = SalesOrder.objects.get(id=sales_order_id)
            sales_order.delete()
            logger.info(f"Sales order with ID '{sales_order_id}' deleted successfully")
            return True
        except SalesOrder.DoesNotExist:
            logger.error(f"Sales order with ID '{sales_order_id}' does not exist")
            return False

    @staticmethod
    def get_sales_order_by_id(sales_order_id):
        try:
            return SalesOrder.objects.get(id=sales_order_id)
        except SalesOrder.DoesNotExist:
            logger.error(f"Sales order with ID '{sales_order_id}' does not exist")
            return None

    @staticmethod
    def get_sales_order_by_order_number(order_number):
        try:
            return SalesOrder.objects.get(order_number=order_number)
        except SalesOrder.DoesNotExist:
            logger.error(
                f"Sales order with order number '{order_number}' does not exist"
            )
            return None

    @staticmethod
    def list_sales_orders():
        return SalesOrder.objects.all().order_by("-created_at")
