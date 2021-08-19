from http import HTTPStatus


async def test_info(async_api_client):
    status, res = await async_api_client.info()
    assert status == HTTPStatus.OK
    assert 'name' in res
    assert 'version' in res


def test_sync_info(sync_api_client):
    status, res = sync_api_client.info()
    assert status == HTTPStatus.OK
    assert 'name' in res
    assert 'version' in res
