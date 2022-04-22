import pytest
from apis.tests.data import get_fake_user_json_payload


@pytest.mark.django_db
def test_register_user_success(api_client):
    endpoint = '/api/profile/'

    user_payload = get_fake_user_json_payload()
    response = api_client().post(
        endpoint,
        data=user_payload,
        format='json'
    )

    assert response.status_code == 201

@pytest.mark.django_db
def test_register_user_email_mandatory(api_client):
    endpoint = '/api/profile/'

    user_payload = get_fake_user_json_payload()
    user_payload['email'] = ""
    response = api_client().post(
        endpoint,
        data=user_payload,
        format='json'
    )

    print(response.content)
    assert response.status_code == 400
    assert response.content == b'{"email":["This field may not be blank."]}'


@pytest.mark.django_db
def test_register_user_name_mandatory(api_client):
    endpoint = '/api/profile/'

    user_payload = get_fake_user_json_payload()
    user_payload['name'] = ""
    response = api_client().post(
        endpoint,
        data=user_payload,
        format='json'
    )

    print(response.content)
    assert response.status_code == 400
    assert response.content == b'{"name":["This field may not be blank."]}'


@pytest.mark.django_db
def test_register_user_phone_mandatory(api_client):
    endpoint = '/api/profile/'

    user_payload = get_fake_user_json_payload()
    user_payload['phone'] = ""
    response = api_client().post(
        endpoint,
        data=user_payload,
        format='json'
    )

    print(response.content)
    assert response.status_code == 400
    assert response.content == b'{"phone":["This field may not be blank."]}'


@pytest.mark.django_db
def test_register_user_pincode_mandatory(api_client):
    endpoint = '/api/profile/'

    user_payload = get_fake_user_json_payload()
    user_payload['pincode'] = ""
    response = api_client().post(
        endpoint,
        data=user_payload,
        format='json'
    )

    print(response.content)
    assert response.status_code == 400
    assert response.content == b'{"pincode":["This field may not be blank."]}'

