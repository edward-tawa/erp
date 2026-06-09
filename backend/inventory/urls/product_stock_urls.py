from rest_framework.routers import DefaultRouter
from inventroy.views.product_stock_views import ProductStockViewSet


router = DefaultRouter()
router.register(r"", ProductStockViewSet, basename="product-stock")
urlpatterns = router.urls
