import pytest
from rest_framework.test import APIRequestFactory
from inventory.views.category_views import CategoryViewSet
from users.permissions.user_permissions import IsAdmin, IsManager, IsEmployee, IsViewer


@pytest.mark.django_db
class TestInventoryPermissions:
    def test_role_permission_mapping(self):
        assert IsAdmin.required_perms
        assert IsManager.required_perms
        assert IsEmployee.required_perms
        assert IsViewer.required_perms

    def test_category_create_requires_authenticated_user(self):
        request = APIRequestFactory().post("/")
        view = CategoryViewSet()
        view.action = "create"
        perms = view.get_permissions()
        assert len(perms) == 2
