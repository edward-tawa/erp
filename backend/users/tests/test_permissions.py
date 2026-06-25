import pytest
from users.permissions.user_permissions import IsAdmin, IsEmployee
from users.permissions.role_permission_mapping import ROLE_PERMISSION_MAPPING


@pytest.mark.django_db
class TestUserPermissions:
    def test_is_admin_requires_permissions(self):
        assert IsAdmin.required_perms == ROLE_PERMISSION_MAPPING["admin"]

    def test_non_authenticated_user_fails(self):
        perm = IsEmployee()
        request = type(
            "Request", (), {"user": type("Anon", (), {"is_authenticated": False})()}
        )()
        assert not perm.has_permission(request, None)
