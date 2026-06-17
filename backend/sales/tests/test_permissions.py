import pytest
from users.permissions.user_permissions import IsEmployee, IsManager


@pytest.mark.django_db
class TestSalesPermissions:
    def test_permission_classes_exist(self):
        assert IsEmployee is not None
        assert IsManager is not None
