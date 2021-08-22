from typing import Dict, Any

from aiohttp import ClientSession


class Namespace:
    URL: str = None

    def __init__(self, host, url_prefix, signer):
        self._host = host
        self._signer = signer
        self._url_prefix = url_prefix

    def get_auth_headers(self, body: Dict[str, Any]) -> Dict[str, str]:
        return {
            'X-Request-Sign': self._signer.get_sign(body),
            'X-Request-App': self._signer.public_key
        }

    async def _run_query(self, url, method="get", **kwargs):
        async with ClientSession() as session:
            m = getattr(session, method)
            async with m(
                f'{self._host}{self._url_prefix}{url}', **kwargs
            ) as resp:
                return resp.status, await resp.json()

    async def _get(self, url, **kwargs):
        headers = self.get_auth_headers({"url": f'{self._url_prefix}{url}'})
        if 'headers' in kwargs:
            kwargs['headers'].update(headers)
        else:
            kwargs['headers'] = headers
        return await self._run_query(url, **kwargs)

    async def _post(self, url, **kwargs):
        headers = self.get_auth_headers(kwargs.get('json', {}))
        if 'headers' in kwargs:
            kwargs['headers'].update(headers)
        else:
            kwargs['headers'] = headers
        return await self._run_query(url, 'post', **kwargs)

    async def _put(self, url, **kwargs):
        headers = self.get_auth_headers(kwargs.get('json', {}))
        if 'headers' in kwargs:
            kwargs['headers'].update(headers)
        else:
            kwargs['headers'] = headers
        return await self._run_query(url, 'put', **kwargs)

    async def _delete(self, url, **kwargs):
        headers = self.get_auth_headers({"url": f'{self._url_prefix}{url}'})
        if 'headers' in kwargs:
            kwargs['headers'].update(headers)
        else:
            kwargs['headers'] = headers
        return await self._run_query(url, 'delete', **kwargs)
