import pytest
from flora_api_client.client import FloraAsyncApiClient, FloraSyncApiClient


@pytest.fixture
def async_api_client():
    return FloraAsyncApiClient(app_id='yyyyyyy',
                               app_key='xxxxxxxxxxxxxxxxxxxxxxxxxxx',
                               host='http://0.0.0.0:8081')


@pytest.fixture
def sync_api_client():
    return FloraSyncApiClient(app_id='yyyyyyy',
                              app_key='xxxxxxxxxxxxxxxxxxxxxxxxxxx',
                              host='http://0.0.0.0:8081')
