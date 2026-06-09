from inventory.urls.product_urls import urlpatterns as product_urls
from inventory.urls.stock_movement_urls import urlpatterns as stock_movement_urls
from inventory.urls.stock_take_urls import urlpatterns as stock_take_urls
from inventory.urls.stock_take_item_urls import urlpatterns as stock_take_item_urls
from inventory.urls.product_stock_urls import urlpatterns as product_stock_urls


__all__ = [
    "product_urls",
    "stock_movement_urls",
    "stock_take_urls",
    "stock_take_item_urls",
    "product_stock_urls",
]
