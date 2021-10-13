from typing import Dict, Any, Union
from urllib.parse import urlencode
from http import HTTPStatus

from aiohttp import ClientSession

from flora_api_client.presentations.base import Querystring


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

    async def _run_query(self, url, method="get", *,
                         long_token: str = "", **kwargs):
        async with ClientSession() as session:
            m = getattr(session, method)
            async with m(
                f'{self._host}{self._url_prefix}{url}', **kwargs
            ) as resp:
                # проверяем на необходимость обновления токена
                if resp.status != HTTPStatus.FORBIDDEN:
                    return resp.status, await resp.json(), None
                body = await resp.json()
                err = body.get('error', {})
                err_code = err.get("error_code", 0)
                first_resp_status = resp.status
                if err_code != 8:
                    return first_resp_status, body, None
            async with session.post(
                f'{self._host}{self._url_prefix}/auth/renew/',
                json={"token": long_token},
                **kwargs
            ) as r:
                if r.status != HTTPStatus.OK:
                    return first_resp_status, body, None
                new_tokens = await r.json()
            # повторяем запрос с новым токеном
            kwargs['headers']['X-Auth-Token'] = new_tokens['token']
            async with m(
                f'{self._host}{self._url_prefix}{url}', **kwargs
            ) as resp:
                return resp.status, await resp.json(), new_tokens

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

    def build_url(self, query_params: Querystring = None, *,
                  postfix_url: Union[str, int] = '', url: str = None):
        query_string = ''
        if query_params:
            d = query_params.as_dict()
            p = {key: d[key] for key in d if d[key] is not None}
            query_string = f'?{urlencode(p)}'
        if url is None:
            url = self.URL
        return f'{url}{postfix_url}{query_string}'
