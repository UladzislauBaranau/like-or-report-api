import pytest

from django.contrib.auth import get_user_model

from rest_framework.test import APIClient

User = get_user_model()


@pytest.fixture
def test_user(db):
    user = User.objects.create_user(
        username="testuser",
        email="testemail@test.com",
        password="testpass1",
    )
    return user


@pytest.fixture
def auth_client_user(test_user):
    client = APIClient()
    client.force_authenticate(test_user)
    return client
