from rest_framework.routers import DefaultRouter
from sales.views.receipt_views import ReceiptViewSet
from django.urls import path, include


router = DefaultRouter()
router.register(r"receipts", ReceiptViewSet, basename="receipt")
urlpatterns = [
    path("", include(router.urls)),
]
