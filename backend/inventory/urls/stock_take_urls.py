from rest_framework.routers import DefaultRouter
from inventroy.views.stock_take_views import StockTakeViewSet


router = DefaultRouter()
router.register(r"", StockTakeViewSet, basename="stock-take")
urlpatterns = router.urls
