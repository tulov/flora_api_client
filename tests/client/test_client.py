from http import HTTPStatus


async def test_info(api_client):
    status, res = await api_client.info()
    assert status == HTTPStatus.OK
    assert 'name' in res
    assert 'version' in res
