from rest_framework.permissions import BasePermission
from users.permissions.role_permission_mapping import ROLE_PERMISSION_MAPPING


class BaseRolePermission(BasePermission):
    required_perms = []

    def has_permission(self, request, view):
        user = request.user
        if not user.is_authenticated:
            return False

        for perm in self.required_perms:
            if not user.has_perm(perm):
                return False

        return True


class IsAdmin(BaseRolePermission):
    required_perms = ROLE_PERMISSION_MAPPING.get("admin", [])


class IsManager(BaseRolePermission):
    required_perms = ROLE_PERMISSION_MAPPING.get("manager", [])


class IsEmployee(BaseRolePermission):
    required_perms = ROLE_PERMISSION_MAPPING.get("employee", [])


class IsViewer(BaseRolePermission):
    required_perms = ROLE_PERMISSION_MAPPING.get("viewer", [])
