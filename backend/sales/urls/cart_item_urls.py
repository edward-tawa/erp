from rest_framework.routers import DefaultRouter
from django.urls import path, include
from sales.views.cart_item_views import CartItemViewSet


router = DefaultRouter()
router.register(r"cart-items", CartItemViewSet, basename="cartitem")
urlpatterns = [
    path("", include(router.urls)),
]
