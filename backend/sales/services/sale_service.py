from django.db import transaction
from loguru import logger
from sales.models.sale_model import Sale


class SaleService:
    @staticmethod
    @transaction.atomic
    def create_sale(*, sales_order, user, receipt, notes=None):
        logger.info(f"Creating sale for sales order '{sales_order.order_number}'")
        try:
            sale = Sale.objects.create(
                sales_order=sales_order,
                user=user,
                receipt=receipt,
                notes=notes,
            )
            logger.info(
                f"Sale '{sale.sale_reference}' created for sales order '{sales_order.order_number}'"
            )
        except Exception as e:
            logger.error(f"Error occurred while creating sale: {e}")
            raise

        return sale

    @staticmethod
    @transaction.atomic
    def update_sale(sale_id, **updated_fields):
        try:
            sale = Sale.objects.get(id=sale_id)
            for field, value in updated_fields.items():
                setattr(sale, field, value)
            sale.save()
            logger.info(f"Sale with ID '{sale_id}' updated successfully")
            return sale
        except Sale.DoesNotExist:
            logger.error(f"Sale with ID '{sale_id}' does not exist")
            raise

    @staticmethod
    @transaction.atomic
    def delete_sale(sale_id):
        try:
            sale = Sale.objects.get(id=sale_id)
            sale.delete()
            logger.info(f"Sale with ID '{sale_id}' deleted successfully")
            return True
        except Sale.DoesNotExist:
            logger.error(f"Sale with ID '{sale_id}' does not exist")
            return False

    @staticmethod
    def get_sale_by_id(sale_id):
        try:
            return Sale.objects.get(id=sale_id)
        except Sale.DoesNotExist:
            logger.error(f"Sale with ID '{sale_id}' does not exist")
            return None

    @staticmethod
    def list_sales():
        return Sale.objects.all().order_by("-created_at")
