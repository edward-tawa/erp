from django.db import transaction
from loguru import logger
from sales.models.payment_model import Payment


class PaymentService:
    @staticmethod
    @transaction.atomic
    def create_payment(*, receipt, user, payment_type, total_amount, denomination):
        try:
            payment = Payment.objects.create(
                receipt=receipt,
                user=user,
                payment_type=payment_type,
                total_amount=total_amount,
                denomination=denomination,
            )
            logger.info(
                f"Payment of {payment.total_amount} {payment.denomination} for receipt '{receipt.receipt_reference}' created successfully"
            )
            return payment
        except Exception as e:
            logger.error(f"Error occurred while creating payment: {e}")
            return None

    @staticmethod
    @transaction.atomic
    def update_payment(payment_id, **updated_fields):
        try:
            payment = Payment.objects.select_for_update().get(id=payment_id)
            for field, value in updated_fields.items():
                setattr(payment, field, value)
            payment.save()
            logger.info(f"Payment with ID '{payment_id}' updated successfully")
            return payment
        except Payment.DoesNotExist:
            logger.error(f"Payment with ID '{payment_id}' does not exist")
            return None

    @staticmethod
    @transaction.atomic
    def delete_payment(payment_id):
        try:
            payment = Payment.objects.get(id=payment_id)
            payment.delete()
            logger.info(f"Payment with ID '{payment_id}' deleted successfully")
            return True
        except Payment.DoesNotExist:
            logger.error(f"Payment with ID '{payment_id}' does not exist")
            return False

    @staticmethod
    def get_payment_by_id(payment_id):
        try:
            return Payment.objects.get(id=payment_id)
        except Payment.DoesNotExist:
            logger.error(f"Payment with ID '{payment_id}' does not exist")
            return None

    def get_payments_by_receipt(receipt_id):
        try:
            return Payment.objects.filter(receipt_id=receipt_id)
        except Exception as e:
            logger.error(
                f"Error occurred while retrieving payments for receipt ID '{receipt_id}': {e}"
            )
            return None

    def get_payments_by_denomination(denomination):
        try:
            return Payment.objects.filter(denomination=denomination)
        except Exception as e:
            logger.error(
                f"Error occurred while retrieving payments for denomination '{denomination}': {e}"
            )
            return None
