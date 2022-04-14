import json


def test_content_creation_without_login(api_client):
    endpoint = '/api/content/'

    expected_json = {
            'title': 'Test Title',
            'body': 'test body',
            'summary': 'test summary',
            'document': 'https://www.google.com',
            'categories': 'tech,account'
        }

    response = api_client().post(
        endpoint,
        data=expected_json,
        format='json'
    )

    assert response.status_code == 401


def test_content_creation_with_login(content, api_client, auth_token):
    endpoint = '/api/content/'

    expected_json = {
            'title': 'Test Title',
            'body': 'test body',
            'summary': 'test summary',
            'document': 'https://www.google.com',
            'categories': 'tech,account'
        }
    print(auth_token)
    response = api_client().post(
        endpoint,
        headers={'Authorization': 'Token 8f811308cb1452c0a47c095becfe5a7fc75a248a'},
        data=expected_json,
        format='json'
    )

    assert response.status_code == 201
    assert json.loads(response.content) == expected_json


def test_content_list(content, api_client):
    endpoint = '/api/content/'
    response = api_client().get(
        endpoint
    )

    assert response.status_code == 200
    assert len(json.loads(response.content)) == 1


def test_content_list_search(content, api_client):
    endpoint = '/api/content/?search=test'
    response = api_client().get(
        endpoint
    )

    assert response.status_code == 200
    assert len(json.loads(response.content)) == 1
