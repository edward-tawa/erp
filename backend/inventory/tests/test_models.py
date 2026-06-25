import pytest
from inventory.tests.factories import (
    CategoryFactory,
    ProductFactory,
    ProductStockFactory,
    StockMovementFactory,
    StockTakeFactory,
    StockTakeItemFactory,
)


@pytest.mark.django_db
class TestInventoryModels:
    def test_category_str(self):
        category = CategoryFactory(name="Hardware")
        assert str(category) == "Hardware"

    def test_product_str(self):
        product = ProductFactory(name="Hammer")
        assert str(product) == "Hammer"

    def test_product_stock_str(self):
        stock = ProductStockFactory(quantity=7)
        assert str(stock) == f"{stock.product.name} - 7 units"

    def test_stock_movement_str(self):
        movement = StockMovementFactory(quantity=4)
        assert "4 units" in str(movement)
        assert movement.get_movement_type_display() in str(movement)

    def test_stock_take_generates_reference_number(self):
        stock_take = StockTakeFactory(reference_number="")
        assert stock_take.reference_number.startswith("ST-")

    def test_stock_take_properties(self):
        stock_take = StockTakeFactory()
        StockTakeItemFactory(stock_take=stock_take, quantity=2)
        StockTakeItemFactory(stock_take=stock_take, quantity=5)
        assert stock_take.number_of_products_counted == 2
        assert stock_take.total_units_counted == 7

    def test_stock_take_item_str(self):
        item = StockTakeItemFactory(quantity=6)
        assert str(item) == f"Stock Take Item - {item.product.name} - 6 units"
