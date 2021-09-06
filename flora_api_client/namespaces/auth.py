from http import HTTPStatus
from typing import Union

from flora_api_client.utils.decorators import expectations
from ..presentations.auth import AuthResponse, AuthRequest
from ..schemas import AuthResponseSchema, ErrorResponseSchema
from ..namespaces.base import Namespace


class AuthNamespace(Namespace):
    URL = '/auth/'

    @expectations(schema=AuthResponseSchema,
                  expected_code=HTTPStatus.OK)
    async def authenticate(
        self, data: AuthRequest, **kwargs
    ) -> (int, Union[AuthResponse, ErrorResponseSchema]):
        return await self._post(self.URL, json=data.as_dict(), **kwargs)
