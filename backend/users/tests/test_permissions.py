import pytest
from users.permissions.user_permissions import IsAdmin, IsEmployee


@pytest.mark.django_db
class TestUserPermissions:
    def test_is_admin_requires_permissions(self):
        assert IsAdmin.required_perms == [
            "users.add_user",
            "users.change_user",
            "users.delete_user",
            "users.view_user",
        ]

    def test_non_authenticated_user_fails(self):
        perm = IsEmployee()
        request = type(
            "Request", (), {"user": type("Anon", (), {"is_authenticated": False})()}
        )()
        assert not perm.has_permission(request, None)
