import pytest
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate
from sales.tests.factories import CustomerFactory
from sales.views.customer_views import CustomerViewSet
from sales.views.sales_order_views import SalesOrderViewSet
from sales.views.cart_views import CartViewSet
from users.tests.factories import UserFactory


@pytest.mark.django_db
class TestSalesViews:
    def test_customer_list_requires_manager_or_employee(self):
        factory = APIRequestFactory()
        request = factory.get("/api/sales/customers/")
        response = CustomerViewSet.as_view({"get": "list"})(request)
        assert response.status_code in (
            status.HTTP_401_UNAUTHORIZED,
            status.HTTP_403_FORBIDDEN,
        )

    def test_manager_can_create_customer(self):
        manager = UserFactory(is_staff=True, role="manager")
        factory = APIRequestFactory()
        request = factory.post(
            "/api/sales/customers/",
            {"name": "Acme", "email": "acme@example.com"},
            format="json",
        )
        force_authenticate(request, user=manager)
        response = CustomerViewSet.as_view({"post": "create"})(request)
        assert response.status_code == status.HTTP_201_CREATED

    def test_sales_order_create_uses_manager_permission(self):
        manager = UserFactory(is_staff=True, role="manager")
        customer = CustomerFactory()
        factory = APIRequestFactory()
        request = factory.post(
            "/api/sales/sales-orders/",
            {"customer": customer.id, "status": "PENDING", "total_amount": "10.00"},
            format="json",
        )
        force_authenticate(request, user=manager)
        response = SalesOrderViewSet.as_view({"post": "create"})(request)
        assert response.status_code in (
            status.HTTP_201_CREATED,
            status.HTTP_400_BAD_REQUEST,
        )

    def test_cart_create_requires_manager(self):
        manager = UserFactory(is_staff=True, role="manager")
        user = UserFactory()
        factory = APIRequestFactory()
        request = factory.post("/api/sales/carts/", {"user": user.id}, format="json")
        force_authenticate(request, user=manager)
        response = CartViewSet.as_view({"post": "create"})(request)
        assert response.status_code in (
            status.HTTP_201_CREATED,
            status.HTTP_400_BAD_REQUEST,
        )
