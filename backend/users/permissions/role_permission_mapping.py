ROLE_PERMISSION_MAPPING = {
    "admin": [
        "users.add_user",
        "users.change_user",
        "users.delete_user",
        "users.view_user",
    ],
    "manager": [
        "users.add_user",
        "users.change_user",
        "users.view_user",
    ],
    "employee": [
        "users.view_user",
    ],
    "viewer": [
        "users.view_user",
    ],
}
