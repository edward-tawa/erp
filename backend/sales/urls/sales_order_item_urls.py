from rest_framework.routers import DefaultRouter
from sales.views.sales_order_item_views import SalesOrderItemViewSet
from django.urls import path, include


router = DefaultRouter()
router.register(r"sales-order-items", SalesOrderItemViewSet, basename="salesorderitem")
urlpatterns = [
    path("", include(router.urls)),
]
