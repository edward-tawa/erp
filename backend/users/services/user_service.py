from django.db import transactions
from users.models import CustomUser


class UserService:
    @staticmethod
    @transactions.atomic
    def create_user(email, username, password, **extra_fields):
        return CustomUser.objects.create_user(
            email=email, username=username, password=password, **extra_fields
        )

    @staticmethod
    @transactions.atomic
    def create_superuser(email, username, password, **extra_fields):
        return CustomUser.objects.create_superuser(
            email=email, username=username, password=password, **extra_fields
        )

    @staticmethod
    def get_user_by_email(email):
        try:
            return CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            return None

    @staticmethod
    def get_user_by_id(user_id):
        try:
            return CustomUser.objects.get(id=user_id)
        except CustomUser.DoesNotExist:
            return None

    @staticmethod
    @transactions.atomic
    def update_user(user_id, **updated_fields):
        user = UserService.get_user_by_id(user_id)
        if not user:
            return None
        for key, value in updated_fields.items():
            setattr(user, key, value)

        user.save()
        return user

    @staticmethod
    def get_current_user(request):
        if request.user.is_authenticated:
            return request.user
        return None

    @staticmethod
    @transactions.atomic
    def delete_user(user_id):
        user = UserService.get_user_by_id(user_id)
        if not user:
            return False
        user.delete()
        return True

    @staticmethod
    def get_all_users(**filters):
        """Get all users with optional filtering"""
        queryset = CustomUser.objects.all()
        for key, value in filters.items():
            queryset = queryset.filter(**{key: value})
        return queryset

    @staticmethod
    def get_active_users():
        """Get all active users"""
        return CustomUser.objects.filter(is_active=True)

    @staticmethod
    def get_users_by_role(role):
        """Get users by role/permission"""
        # Adjust based on your CustomUser model
        return CustomUser.objects.filter(groups__name=role)
