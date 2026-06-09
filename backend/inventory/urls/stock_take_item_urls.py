from rest_framework.routers import DefaultRouter
from inventory.views.stock_take_item_views import StockTakeItemViewSet


router = DefaultRouter()
router.register(r"", StockTakeItemViewSet, basename="stock-take-item")
urlpatterns = router.urls
