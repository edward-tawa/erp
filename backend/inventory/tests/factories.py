import factory
from decimal import Decimal
from django.utils import timezone
from inventory.models.category_model import Category
from inventory.models.product_model import Product
from inventory.models.product_stock_model import ProductStock
from inventory.models.stock_movement_model import StockMovement
from inventory.models.stock_take_item_model import StockTakeItem
from inventory.models.stock_take_model import StockTake


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Sequence(lambda n: f"Category {n}")
    description = factory.Faker("sentence")


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    name = factory.Sequence(lambda n: f"Product {n}")
    category = factory.SubFactory(CategoryFactory)
    description = factory.Faker("sentence")
    price = Decimal("10.00")
    sku = factory.Sequence(lambda n: f"SKU-{n:05d}")


class ProductStockFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ProductStock

    product = factory.SubFactory(ProductFactory)
    quantity = 10
    min_stock_level = 5


class StockMovementFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = StockMovement

    product = factory.SubFactory(ProductFactory)
    quantity = 2
    movement_type = StockMovement.MovementType.PURCHASE


class StockTakeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = StockTake

    reference_number = factory.Sequence(lambda n: f"ST-TEST-{n:05d}")
    notes = factory.Faker("sentence")
    taken_by = None
    date_taken = factory.LazyFunction(timezone.now)
    status = StockTake.Status.ONGOING


class StockTakeItemFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = StockTakeItem

    stock_take = factory.SubFactory(StockTakeFactory)
    product = factory.SubFactory(ProductFactory)
    quantity = 3
