from http import HTTPStatus
from typing import Union

from flora_api_client.utils.decorators import expectations
from ..presentations.auth import (
    AuthResponse, AuthRequest, RenewTokenRequest, RenewTokenResponse
)
from ..presentations.error import ErrorResponse
from ..schemas import (
    AuthResponseSchema, RenewTokenResponseSchema
)
from ..namespaces.base import Namespace


class AuthNamespace(Namespace):
    URL = '/auth/'

    @expectations(schema=AuthResponseSchema,
                  expected_code=HTTPStatus.OK)
    async def authenticate(
        self, data: AuthRequest, **kwargs
    ) -> (int, Union[AuthResponse, ErrorResponse]):
        return await self._post(self.URL, json=data.as_dict(), **kwargs)

    @expectations(schema=RenewTokenResponseSchema,
                  expected_code=HTTPStatus.OK)
    async def renew(
        self, data: RenewTokenRequest, **kwargs
    ) -> (int, Union[RenewTokenResponse, ErrorResponse]):
        return await self._post(f'{self.URL}renew/',
                                json=data.as_dict(), **kwargs)
