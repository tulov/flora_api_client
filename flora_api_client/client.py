import requests
from typing import Dict, Any
from aiohttp import ClientSession
from flora_api_client.auth.singer import Singer


class FloraApiClient:
    def __init__(self, *, app_id: str, app_key: str,
                 host: str, url_prefix: str = '/api/v1'):
        self._host = host
        self._url_prefix = url_prefix
        self._signer = Singer(private_key=app_key, public_key=app_id)

    @property
    def info_url(self) -> str:
        return f'{self._url_prefix}/info/'

    def get_auth_headers(self, body: Dict[str, Any]) -> Dict[str, str]:
        return {
            'X-Request-Sign': self._signer.get_sign(body),
            'X-Request-App': self._signer.public_key
        }


class FloraAsyncApiClient(FloraApiClient):
    async def info(self):
        headers = self.get_auth_headers({"url": self.info_url})
        async with ClientSession() as session:
            async with session.get(
                f'{self._host}{self.info_url}', headers=headers
            ) as resp:
                return resp.status, await resp.json()


class FloraSyncApiClient(FloraApiClient):
    def info(self):
        headers = self.get_auth_headers({"url": self.info_url})
        resp = requests.get(f'{self._host}{self.info_url}', headers=headers)
        return resp.status_code, resp.json()
