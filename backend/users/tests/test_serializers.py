import pytest
from users.serializers.user_serializer import UserSerializer
from users.tests.factories import UserFactory


@pytest.mark.django_db
class TestUserSerializer:
    def test_create_user_serializer_valid(self):
        serializer = UserSerializer(
            data={
                "email": "new@example.com",
                "username": "newuser",
                "password": "password123",
                "first_name": "New",
                "last_name": "User",
                "role": "employee",
            }
        )
        assert serializer.is_valid(), serializer.errors

    def test_reject_duplicate_email(self):
        UserFactory(email="dup@example.com")
        serializer = UserSerializer(
            data={
                "email": "dup@example.com",
                "username": "otheruser",
                "password": "password123",
                "role": "employee",
            }
        )
        assert not serializer.is_valid()
        assert "email" in serializer.errors
