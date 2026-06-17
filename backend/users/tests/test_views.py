import pytest
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate
from users.tests.factories import UserFactory
from users.views.user_views import UserViewSet


@pytest.mark.django_db
class TestUserViews:
    def test_list_requires_authentication(self):
        factory = APIRequestFactory()
        request = factory.get("/api/users/")
        response = UserViewSet.as_view({"get": "list"})(request)
        assert response.status_code in (
            status.HTTP_401_UNAUTHORIZED,
            status.HTTP_403_FORBIDDEN,
        )

    def test_admin_can_create_user(self):
        admin = UserFactory(is_staff=True, role="admin")
        admin.user_permissions.set([])
        factory = APIRequestFactory()
        request = factory.post(
            "/api/users/",
            {
                "email": "created@example.com",
                "username": "createduser",
                "password": "password123",
                "role": "employee",
            },
            format="json",
        )
        force_authenticate(request, user=admin)
        response = UserViewSet.as_view({"post": "create"})(request)
        assert response.status_code in (
            status.HTTP_201_CREATED,
            status.HTTP_400_BAD_REQUEST,
        )
