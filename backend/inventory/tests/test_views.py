import pytest
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate
from inventory.tests.factories import ProductFactory
from inventory.views.category_views import CategoryViewSet
from inventory.views.product_stock_views import ProductStockViewSet
from users.tests.factories import UserFactory


@pytest.mark.django_db
class TestInventoryViews:
    def test_category_list_requires_authentication(self):
        factory = APIRequestFactory()
        request = factory.get("/api/inventory/categories/")
        response = CategoryViewSet.as_view({"get": "list"})(request)
        assert response.status_code in (
            status.HTTP_401_UNAUTHORIZED,
            status.HTTP_403_FORBIDDEN,
        )

    def test_admin_can_create_category(self):
        user = UserFactory(is_staff=True)
        user.role = "admin"
        user.save(update_fields=["role"])
        factory = APIRequestFactory()
        request = factory.post(
            "/api/inventory/categories/",
            {"name": "Tools", "description": "x"},
            format="json",
        )
        force_authenticate(request, user=user)
        response = CategoryViewSet.as_view({"post": "create"})(request)
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data["name"] == "Tools"

    def test_product_stock_crud(self):
        user = UserFactory(is_staff=True)
        user.role = "admin"
        user.save(update_fields=["role"])
        product = ProductFactory()
        factory = APIRequestFactory()
        request = factory.post(
            "/api/inventory/product-stocks/",
            {"product": product.id, "quantity": 10, "min_stock_level": 2},
            format="json",
        )
        force_authenticate(request, user=user)
        response = ProductStockViewSet.as_view({"post": "create"})(request)
        assert response.status_code == status.HTTP_201_CREATED
