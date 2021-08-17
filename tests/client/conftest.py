import pytest
from flora_api_client.client import FloraApiClient


@pytest.fixture
def api_client():
    return FloraApiClient(app_id='yyyyyyy',
                          app_key='xxxxxxxxxxxxxxxxxxxxxxxxxxx',
                          host='http://0.0.0.0:8081')
