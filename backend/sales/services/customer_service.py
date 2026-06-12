from django.db import transaction
from sales.models.customer_model import Customer
from loguru import logger
from django.core.exceptions import ValidationError


class CustomerService:
    @staticmethod
    @transaction.atomic
    def create_customer(name, email=None, phone_number=None, address=None):
        customer = Customer.objects.create(
            name=name, email=email, phone_number=phone_number, address=address
        )
        logger.info(
            f"Customer '{customer.name}' created successfully with ID '{customer.id}'"
        )
        return customer

    @staticmethod
    @transaction.atomic
    def update_customer(customer_id, **updated_fields):
        try:
            customer = Customer.objects.select_for_update().get(id=customer_id)
            for field, value in updated_fields.items():
                setattr(customer, field, value)
            customer.full_clean()  # validate fields
            customer.save()
            logger.info(f"Customer with ID '{customer_id}' updated successfully")
            return customer
        except Customer.DoesNotExist:
            logger.error(f"Customer with ID '{customer_id}' does not exist")
            return None
        except ValidationError as e:
            logger.error(f"Validation failed for customer '{customer_id}': {e}")
            return None

    @staticmethod
    @transaction.atomic
    def delete_customer(customer_id):
        try:
            customer = Customer.objects.get(id=customer_id)
            customer.delete()
            logger.info(f"Customer with ID '{customer_id}' deleted successfully")
            return True
        except Customer.DoesNotExist:
            logger.error(f"Customer with ID '{customer_id}' does not exist")
            return False

    @staticmethod
    def get_customer_by_id(customer_id):
        try:
            return Customer.objects.get(id=customer_id)
        except Customer.DoesNotExist:
            logger.error(f"Customer with ID '{customer_id}' does not exist")
            return None

    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except Customer.DoesNotExist:
            logger.error(f"Customer with email '{email}' does not exist")
            return None

    @staticmethod
    def get_all_customers():
        return Customer.objects.all()
