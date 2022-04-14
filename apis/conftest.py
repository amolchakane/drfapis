import pytest
from django.test import RequestFactory
from mixer.backend.django import mixer
from rest_framework.test import APIClient


@pytest.fixture
def factory():
    """Return RequestFactory object"""
    return RequestFactory()


@pytest.fixture
def content(db):
    """Creates content using mixer package"""
    user_profile = mixer.blend('apis.UserProfile')
    return mixer.blend('apis.Content', user_profile=user_profile, title="My Test Content", body="Sample description",
                       summary="Test summary", document="https://www.test.com/test.pdf", categories="test1, test2")


@pytest.fixture
def api_client():
    return APIClient


@pytest.fixture
def auth_token():
    return '8f811308cb1452c0a47c095becfe5a7fc75a248a'
