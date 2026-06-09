from inventroy.models.category_model import Category
from django.db import transaction
from loguru import logger


class CategoryService:
    @staticmethod
    @transaction.atomic
    def create_category(*, name, description=None):
        category = Category.objects.create(name=name, description=description)
        if category:
            logger.info(f"Created category '{category.name}'")
        else:
            logger.error(f"Failed to create category '{name}'")
        return category

    @staticmethod
    @transaction.atomic
    def update_category(category_id, **updated_fields):
        try:
            category = Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            logger.error(f"Category with ID '{category_id}' does not exist")
            return None

        for key, value in updated_fields.items():
            setattr(category, key, value)

        category.save()
        logger.info(f"Category with ID '{category_id}' updated successfully")
        return category

    @staticmethod
    @transaction.atomic
    def delete_category(category_id):
        try:
            category = Category.objects.get(id=category_id)
            category.delete()
            logger.info(f"Category with ID '{category_id}' deleted successfully")
            return True
        except Category.DoesNotExist:
            logger.error(f"Category with ID '{category_id}' does not exist")
            return False

    @staticmethod
    def get_category_by_id(category_id):
        try:
            return Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            logger.error(f"Category with ID '{category_id}' does not exist")
            return None

    @staticmethod
    def get_category_by_name(name):
        try:
            return Category.objects.get(name=name)
        except Category.DoesNotExist:
            logger.error(f"Category with name '{name}' does not exist")
            return None

    @staticmethod
    def list_categories():
        return Category.objects.all().order_by("-id")
