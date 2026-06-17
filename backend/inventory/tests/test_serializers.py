import pytest
from inventory.serializers.category_serializer import CategorySerializer
from inventory.serializers.product_serializer import ProductSerializer
from inventory.serializers.product_stock_serializer import ProductStockSerializer
from inventory.serializers.stock_movement_serializer import StockMovementSerializer
from inventory.serializers.stock_take_item_serializer import StockTakeItemSerializer
from inventory.serializers.stock_take_serializer import StockTakeSerializer
from inventory.tests.factories import (
    CategoryFactory,
    ProductFactory,
)
from users.tests.factories import UserFactory


@pytest.mark.django_db
class TestInventorySerializers:
    def test_category_serializer_validates_required_name(self):
        serializer = CategorySerializer(data={"description": "x"})
        assert not serializer.is_valid()
        assert "name" in serializer.errors

    def test_product_serializer_requires_price_and_sku(self):
        serializer = ProductSerializer(data={"name": "Widget"})
        assert not serializer.is_valid()
        assert "price" in serializer.errors
        assert "sku" in serializer.errors

    def test_product_serializer_accepts_category(self):
        category = CategoryFactory()
        serializer = ProductSerializer(
            data={
                "name": "Widget",
                "price": "12.50",
                "sku": "SKU-123",
                "category": category.id,
            }
        )
        assert serializer.is_valid(), serializer.errors

    def test_product_stock_serializer_requires_product_and_quantity(self):
        serializer = ProductStockSerializer(data={})
        assert not serializer.is_valid()
        assert "product" in serializer.errors
        assert "quantity" in serializer.errors

    def test_stock_movement_serializer_requires_choice_field(self):
        product = ProductFactory()
        serializer = StockMovementSerializer(
            data={"product": product.id, "quantity": 2}
        )
        assert not serializer.is_valid()
        assert "movement_type" in serializer.errors

    def test_stock_take_serializer_matches_model_fields(self):
        user = UserFactory()
        serializer = StockTakeSerializer(
            data={
                "taken_by": user.id,
                "date_taken": "2026-06-17T00:00:00Z",
                "status": "ongoing",
            }
        )
        assert serializer.is_valid(), serializer.errors

    def test_stock_take_item_serializer_requires_fields(self):
        serializer = StockTakeItemSerializer(data={})
        assert not serializer.is_valid()
        assert "stock_take" in serializer.errors
        assert "product" in serializer.errors
        assert "quantity" in serializer.errors
