from rest_framework.routers import DefaultRouter
from inventroy.views.product_views import ProductViewSet

router = DefaultRouter()
router.register(r"", ProductViewSet, basename="product")
urlpatterns = router.urls
