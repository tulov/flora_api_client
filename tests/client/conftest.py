import pytest
import os
from flora_api_client.client import FloraApiClient

API_SERVER_URL = os.environ.get('TEST_API_SERVER_URL', 'http://0.0.0.0:8081')
PRIVATE_KEY = os.environ.get('TEST_API_PRIVATE_KEY', '')
PUBLIC_KEY = os.environ.get('TEST_API_PUBLIC_KEY', '')


@pytest.fixture
def async_api_client():
    return FloraApiClient(app_id=PUBLIC_KEY,
                          app_key=PRIVATE_KEY,
                          host=API_SERVER_URL)
