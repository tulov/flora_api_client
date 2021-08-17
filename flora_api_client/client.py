from aiohttp import ClientSession
from flora_api_client.auth.singer import Singer


class FloraApiClient:
    def __init__(self, *, app_id: str, app_key: str,
                 host: str, url_prefix: str = '/api/v1'):
        self._host = host
        self._url_prefix = url_prefix
        self._signer = Singer(private_key=app_key, public_key=app_id)

    async def info(self):
        url = f'{self._url_prefix}/info/'
        headers = {
            'X-Request-Sign': self._signer.get_sign({"url": url}),
            'X-Request-App': self._signer.public_key
        }
        async with ClientSession() as session:
            async with session.get(
                f'{self._host}{url}', headers=headers
            ) as resp:
                return resp.status, await resp.json()
