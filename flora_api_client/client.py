from typing import Dict, Any, Union
from aiohttp import ClientSession
from functools import wraps

from flora_api_client.auth.singer import Singer
from flora_api_client.presentations.main import ApplicationInfoResponse
from flora_api_client.schemas.main import ApplicationInfoResponseSchema
from flora_api_client.schemas.error import ErrorResponseSchema


def schema(schema_class):
    def decorate(fn):
        @wraps(fn)
        async def inner(*args, **kwargs):
            code, res = await fn(*args, **kwargs)
            sch = ErrorResponseSchema() if code > 299 else schema_class()
            return code, sch.load(res)
        return inner
    return decorate


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
    @schema(ApplicationInfoResponseSchema)
    async def info(
        self
    ) -> (int, Union[ApplicationInfoResponse, ErrorResponseSchema]):
        headers = self.get_auth_headers({"url": self.info_url})
        async with ClientSession() as session:
            async with session.get(
                f'{self._host}{self.info_url}', headers=headers
            ) as resp:
                return resp.status, await resp.json()
