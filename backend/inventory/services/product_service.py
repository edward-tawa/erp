from inventroy.models.product_model import Product
from django.db import transaction
from loguru import logger


class ProductService:
    @staticmethod
    @transaction.atomic
    def create_product(*, name, category, description, price, sku, image=None):
        product = Product.objects.create(
            name=name,
            category=category,
            description=description,
            price=price,
            sku=sku,
            image=image,
        )
        if product:
            logger.info(f"Created product '{product.name}' with SKU '{product.sku}'")
        else:
            logger.error(f"Failed to create product '{name}' with SKU '{sku}'")
        return product

    @staticmethod
    @transaction.atomic
    def update_product(product_id, **updated_fields):
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            logger.error(f"Product with ID '{product_id}' does not exist")
            return None

        for key, value in updated_fields.items():
            setattr(product, key, value)

        product.save()
        logger.info(f"Product with ID '{product_id}' updated successfully")
        return product

    @staticmethod
    @transaction.atomic
    def delete_product(product_id):
        try:
            product = Product.objects.get(id=product_id)
            product.delete()
            logger.info(f"Product with ID '{product_id}' deleted successfully")
            return True
        except Product.DoesNotExist:
            logger.error(f"Product with ID '{product_id}' does not exist")
            return False

    @staticmethod
    def get_product_by_id(product_id):
        try:
            return Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            logger.error(f"Product with ID '{product_id}' does not exist")
            return None

    @staticmethod
    def get_product_by_sku(sku):
        try:
            return Product.objects.get(sku=sku)
        except Product.DoesNotExist:
            logger.error(f"Product with SKU '{sku}' does not exist")
            return None

    @staticmethod
    def list_products():
        return Product.objects.all().order_by("-id")
