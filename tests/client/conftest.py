import pytest
from flora_api_client.client import FloraAsyncApiClient


@pytest.fixture
def async_api_client():
    return FloraAsyncApiClient(app_id='yyyyyyy',
                               app_key='xxxxxxxxxxxxxxxxxxxxxxxxxxx',
                               host='http://0.0.0.0:8081')
