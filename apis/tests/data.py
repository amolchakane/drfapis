import json

from rest_framework.test import APIClient


def get_fake_user_json_payload():
    return {
        "email": "test@test.com",
        "name": "Test User",
        "password": "password",
        "phone": "999999999",
        "address": "test address",
        "city": "test",
        "state": "test",
        "country": "test",
        "pincode": "123456"
    }


def get_auth_token():
    client = APIClient()
    register_endpoint = '/api/profile/'

    user_payload = get_fake_user_json_payload()
    response = client.post(
        register_endpoint,
        data=user_payload,
        format='json'
    )
    print("Register response: " + str(response.content, 'UTF-8'))
    # if response.status_code == 200:
    login_endpoint = '/api/login/'
    login_payload = {
        "username": user_payload['email'],
        "password": user_payload['password']
    }
    login_response = client.post(
        login_endpoint,
        data=login_payload,
        format='json'
    )
    print("Login response: " + str(login_response.content, 'UTF-8'))
    response_data = json.loads(login_response.content)
    return response_data['token']
