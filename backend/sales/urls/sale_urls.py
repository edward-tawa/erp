from rest_framework.routers import DefaultRouter
from sales.views.sale_views import SaleViewSet
from django.urls import path, include


router = DefaultRouter()
router.register(r"", SaleViewSet, basename="sale")
urlpatterns = [
    path("", include(router.urls)),
]
