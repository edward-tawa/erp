import pytest
from rest_framework.test import APIClient
from django.core.management import call_command


@pytest.fixture(scope="session", autouse=True)
def setup_rbac(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        call_command("setup_group_permissions")


@pytest.fixture
def api_client():
    return APIClient()
