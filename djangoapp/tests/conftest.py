import pytest

from rest_framework.test import APIClient


@pytest.fixture(scope="session")
def api_client():
    """
    Fixture to provide an API client
    :return: APIClient
    """
    return APIClient()
