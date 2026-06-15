from rest_framework.routers import DefaultRouter
from django.urls import path, include
from sales.views.receipt_item_views import ReceiptItemViewSet


router = DefaultRouter()
router.register(r"receipt-items", ReceiptItemViewSet, basename="receiptitem")
urlpatterns = [
    path("", include(router.urls)),
]
