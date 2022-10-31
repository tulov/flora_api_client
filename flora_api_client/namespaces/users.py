from http import HTTPStatus
from typing import Union

from flora_api_client.utils.decorators import expectations
from ..presentations.auth import RenewTokenResponse
from ..presentations.cities import SearchCitiesResponse
from ..presentations.error import ErrorResponse
from ..presentations.users import (
    RegistrationUserData, User, UsersResponse, ChangePasswordRequest
)
from ..presentations.base import Querystring, SuccessResponse
from ..schemas import UserSchema, UsersResponseSchema, \
    SuccessResponseSchema, SearchCitiesResponseSchema
from ..namespaces.base import Namespace


class UsersNamespace(Namespace):
    URL = '/users/'

    @expectations(schema=UserSchema,
                  expected_code=HTTPStatus.CREATED)
    async def register(
        self, data: RegistrationUserData, **kwargs
    ) -> (int, Union[User, ErrorResponse], RenewTokenResponse):
        return await self._post(self.URL, json=data.as_dict(), **kwargs)

    @expectations(schema=UserSchema,
                  expected_code=HTTPStatus.OK)
    async def get(
        self, user_id: int, **kwargs
    ) -> (int, Union[User, ErrorResponse], RenewTokenResponse):
        return await self._get(f'{self.URL}{user_id}', **kwargs)

    @expectations(schema=UsersResponseSchema,
                  expected_code=HTTPStatus.OK)
    async def all(
        self, query_params: Querystring = None,  **kwargs
    ) -> (int, Union[UsersResponse, ErrorResponse], RenewTokenResponse):
        return await self._get(self.build_url(query_params), **kwargs)

    @expectations(schema=SuccessResponseSchema,
                  expected_code=HTTPStatus.OK)
    async def change_password(
        self, user_id: int, data: ChangePasswordRequest, **kwargs
    ) -> (int, Union[SuccessResponse, ErrorResponse], RenewTokenResponse):
        return await self._put(
            f'{self.URL}{user_id}/password/', json=data.as_dict(), **kwargs)

    @expectations(schema=SearchCitiesResponseSchema)
    async def search(
        self, term: str = None, **kwargs
    ) -> (int, Union[SearchCitiesResponse, ErrorResponse], RenewTokenResponse):
        return await self._get(
            self.build_url(postfix_url=f'search/{term}'), **kwargs
        )

    @expectations(schema=SearchCitiesResponseSchema)
    async def search_ids(
        self, term: str = None, **kwargs
    ) -> (int, Union[SearchCitiesResponse, ErrorResponse], RenewTokenResponse):
        return await self._get(
            self.build_url(postfix_url=f'search-ids/{term}'), **kwargs
        )
