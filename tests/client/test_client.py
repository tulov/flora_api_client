from http import HTTPStatus
from flora_api_client.presentations.main import ApplicationInfoResponse


async def test_info(async_api_client):
    status, res = await async_api_client.info()
    assert status == HTTPStatus.OK
    assert isinstance(res, ApplicationInfoResponse)
