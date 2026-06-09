from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from configurations.shared.created_updated_at import CreatedUpdatedAt
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    def create_user(self, email, username, password, **extra_fields):
        if not email:
            raise ValueError("Email is required")
        if not username:
            raise ValueError("Username is required")
        if not password:
            raise ValueError("Password is required")

        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, username, password, **extra_fields)


class CustomUser(CreatedUpdatedAt, AbstractBaseUser, PermissionsMixin):
    class Roles(models.TextChoices):
        ADMIN = "admin", _("Admin")
        MANAGER = "manager", _("Manager")
        EMPLOYEE = "employee", _("Employee")

    first_name = models.CharField(
        max_length=30, blank=True, null=True, help_text=_("First name")
    )

    last_name = models.CharField(
        max_length=30, blank=True, null=True, help_text=_("Last name")
    )

    email = models.EmailField(unique=True, null=False, help_text=_("Email address"))
    username = models.CharField(
        max_length=150, unique=True, null=False, help_text=_("Username")
    )
    role = models.CharField(
        max_length=20,
        choices=Roles.choices,
        default=Roles.EMPLOYEE,
        verbose_name=_("role"),
        help_text=_("role of the user in the system"),
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    class Meta:
        permissions = [
            ("view_user", "Can view user"),
            ("add_user", "Can add user"),
            ("change_user", "Can change user"),
            ("delete_user", "Can delete user"),
            ("view_user_profile", "Can view user profile"),
            ("change_user_profile", "Can change user profile"),
            ("delete_user_profile", "Can delete user profile"),
        ]

    def __str__(self):
        return self.username
