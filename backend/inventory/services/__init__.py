from inventroy.models.product_model import Product
from django.db import transaction


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
        return product

    @staticmethod
    @transaction.atomic
    def update_product(product_id, **updated_fields):
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return None

        for key, value in updated_fields.items():
            setattr(product, key, value)

        product.save()
        return product
