from django.contrib.auth import get_user_model

from rest_framework.test import APIClient

User = get_user_model()
client = APIClient()


def test_success_user_register(db, test_user):
    endpoint = "/api/v1/users/register/"
    request_data = {
        "username": "testuser1",
        "email": "testemail1@test.com",
        "password": "testpass1",
    }
    response = client.post(endpoint, request_data)

    user = User.objects.get(username="testuser1")
    assert user.username == "testuser1"
    assert user.email == "testemail1@test.com"

    qs_users = User.objects.all()
    assert len(qs_users) == 2
