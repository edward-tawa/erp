from rest_framework.routers import DefaultRouter
from sales.views.sales_order_views import SalesOrderViewSet
from django.urls import path, include


router = DefaultRouter()
router.register(r"sales-orders", SalesOrderViewSet, basename="salesorder")
urlpatterns = [
    path("", include(router.urls)),
]
