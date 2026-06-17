from rest_framework.routers import DefaultRouter
from inventory.views.category_views import CategoryViewSet

router = DefaultRouter()
router.register(r"", CategoryViewSet, basename="category")
urlpatterns = router.urls
