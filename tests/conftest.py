import os
import pytest
import django
import json

from django.urls import reverse


from django.contrib.auth import get_user_model
from rest_framework.test import APIClient


@pytest.fixture
def user(db):
    """Return user instance for testing."""
    user = get_user_model().objects.create_user(
        username="mail@mail.com", password="pass123"
    )
    return user


@pytest.fixture
def logged_in_client(user):
    """Log in test user and return the client."""
    client = APIClient()
    client.login(username="mail@mail.com", password="pass123") is True
    return client


@pytest.fixture
def token(logged_in_client):
    """Token"""
    url = "/api-token-auth/"
    payload = {"username": "mail@mail.com", "password": "pass123"}
    response = logged_in_client.post(url, payload)
    token_payload = json.loads(response.content)
    return token_payload.get("token")
