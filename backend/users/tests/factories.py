import factory
from users.models.user_model import CustomUser


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CustomUser

    email = factory.Sequence(lambda n: f"user{n}@example.com")
    username = factory.Sequence(lambda n: f"user{n}")
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    role = CustomUser.Roles.EMPLOYEE
    is_active = True
    is_staff = False
    password = factory.PostGenerationMethodCall("set_password", "password123")
