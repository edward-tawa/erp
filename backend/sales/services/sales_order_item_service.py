from django.db import transaction
from loguru import logger
from sales.models.sales_order_item_model import SalesOrderItem
from sales.services.sales_order_service import SalesOrderService


class SalesOrderItemService:
    @staticmethod
    @transaction.atomic
    def create_sales_order_item(*, sales_order, product, quantity, unit_price):
        sales_order_item = SalesOrderItem.objects.create(
            sales_order=sales_order,
            product=product,
            quantity=quantity,
            unit_price=unit_price,
        )
        if sales_order_item:
            SalesOrderItemService.calculate_sales_order_total(sales_order)
            logger.info(
                f"Created sales order item for product '{sales_order_item.product.name}' with quantity {sales_order_item.quantity} and unit price {sales_order_item.unit_price} in sales order '{sales_order.order_number}'"
            )
        else:
            logger.error(
                f"Failed to create sales order item for product '{product.name}' with quantity {quantity} and unit price {unit_price} in sales order '{sales_order.order_number}'"
            )
        return sales_order_item

    @staticmethod
    @transaction.atomic
    def bulk_create_items(items_data, sales_order):
        items = [
            SalesOrderItem(
                sales_order=sales_order,
                product=data["product"],
                quantity=data["quantity"],
                unit_price=data["unit_price"],
            )
            for data in items_data
        ]

        SalesOrderItem.objects.bulk_create(items)

        SalesOrderService.update_sales_order_total(sales_order)
        return items

    @staticmethod
    @transaction.atomic
    def update_sales_order_item(sales_order_item_id, **updated_fields):
        try:
            sales_order_item = SalesOrderItem.objects.get(id=sales_order_item_id)
        except SalesOrderItem.DoesNotExist:
            logger.error(
                f"Sales order item with ID '{sales_order_item_id}' does not exist"
            )
            return None

        for key, value in updated_fields.items():
            setattr(sales_order_item, key, value)

        sales_order_item.save()
        SalesOrderItemService.calculate_sales_order_total(sales_order_item.sales_order)
        logger.info(
            f"Sales order item with ID '{sales_order_item_id}' updated successfully"
        )
        return sales_order_item

    @staticmethod
    @transaction.atomic
    def delete_sales_order_item(sales_order_item_id):
        try:
            sales_order_item = SalesOrderItem.objects.get(id=sales_order_item_id)
            sales_order_item.delete()
            SalesOrderItemService.calculate_sales_order_total(
                sales_order_item.sales_order
            )
            logger.info(
                f"Sales order item with ID '{sales_order_item_id}' deleted successfully"
            )
            return True
        except SalesOrderItem.DoesNotExist:
            logger.error(
                f"Sales order item with ID '{sales_order_item_id}' does not exist"
            )
            return False
