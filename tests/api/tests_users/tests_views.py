from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.test import APIClient

User = get_user_model()
client = APIClient()


def test_success_user_register(test_user):
    endpoint = "/api/v1/users/register/"
    request_data = {
        "username": "testuser1",
        "email": "testemail1@test.com",
        "password": "testpass1",
    }

    client.post(endpoint, request_data)

    user = User.objects.get(username="testuser1")
    assert user.username == "testuser1"
    assert user.email == "testemail1@test.com"

    qs_users = User.objects.all()
    assert len(qs_users) == 2


def test_fail_user_register(test_user):
    endpoint = "/api/v1/users/register/"
    request_data = {
        "username": "testuser2",
        "email": "testemail@test.com",  # this email belong test_user
        "password": "testpass2",
    }

    response = client.post(endpoint, request_data)
    assert response.status_code == status.HTTP_400_BAD_REQUEST

    qs_users = User.objects.all()
    assert len(qs_users) == 1


def test_success_login(test_user):
    endpoint = "/api/v1/users/login/"
    request_data = {
        "username": "testuser",
        "password": "testpass1",
    }

    response = client.post(endpoint, request_data)
    assert response.status_code == status.HTTP_200_OK


def test_success_update_user_profile(auth_client_user, test_user):
    pk = test_user.id
    endpoint = f"/api/v1/users/update-profile/{pk}/"
    request_data = {
        "first_name": "unique_first_name",
        "last_name": "unique_last_name",
    }

    response = auth_client_user.patch(endpoint, request_data)
    assert response.status_code == status.HTTP_200_OK

    user = User.objects.get(username="testuser")
    assert user.first_name == "unique_first_name"
    assert user.last_name == "unique_last_name"


def test_change_user_password(auth_client_user, test_user):
    pk = test_user.id
    endpoint = f"/api/v1/users/password-change/{pk}/"
    request_data = {
        "old_password": "testpass1",
        "new_password": "testpass11",
    }

    response = auth_client_user.patch(endpoint, request_data)
    assert response.status_code == status.HTTP_200_OK
