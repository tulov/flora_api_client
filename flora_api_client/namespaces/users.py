from http import HTTPStatus
from typing import Union
from urllib.parse import urlencode

from flora_api_client.utils.decorators import expectations
from ..presentations.users import RegistrationUserData, User, UsersResponse
from ..presentations.base import Querystring
from ..schemas import UserSchema, ErrorResponseSchema, UsersResponseSchema
from ..namespaces.base import Namespace


class UsersNamespace(Namespace):
    URL = '/users/'

    @expectations(schema=UserSchema,
                  expected_code=HTTPStatus.CREATED)
    async def register(
        self, data: RegistrationUserData, **kwargs
    ) -> (int, Union[User, ErrorResponseSchema]):
        return await self._post(self.URL, json=data.as_dict(), **kwargs)

    @expectations(schema=UserSchema,
                  expected_code=HTTPStatus.OK)
    async def get(
        self, user_id: int, **kwargs
    ) -> (int, Union[User, ErrorResponseSchema]):
        return await self._get(f'{self.URL}{user_id}', **kwargs)

    @expectations(schema=UsersResponseSchema,
                  expected_code=HTTPStatus.OK)
    async def all(
        self, query_params: Querystring = None,  **kwargs
    ) -> (int, Union[UsersResponse, ErrorResponseSchema]):
        return await self._get(self.build_url(query_params), **kwargs)
