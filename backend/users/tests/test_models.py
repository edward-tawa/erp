import pytest
from users.tests.factories import UserFactory


@pytest.mark.django_db
class TestUserModel:
    def test_user_str(self):
        user = UserFactory(username="alice")
        assert str(user) == "alice"
