from http import HTTPStatus
from typing import Union

from flora_api_client.utils.decorators import expectations
from ..presentations.auth import RenewTokenResponse
from ..presentations.error import ErrorResponse
from ..presentations.users import RegistrationUserData, User
from ..presentations.partners import BindCityRequestDataclass
from ..presentations.base import SuccessResponse
from ..presentations.cities import CitiesResponse
from ..schemas import UserSchema, SuccessResponseSchema, CitiesResponseSchema
from ..namespaces.base import Namespace


class PartnersNamespace(Namespace):
    URL = '/partners/'

    @expectations(schema=UserSchema,
                  expected_code=HTTPStatus.CREATED)
    async def register(
        self, data: RegistrationUserData, **kwargs
    ) -> (int, Union[User, ErrorResponse], RenewTokenResponse):
        return await self._post(self.URL, json=data.as_dict(), **kwargs)

    @expectations(schema=SuccessResponseSchema)
    async def bind_city(
        self, id_: int, data: BindCityRequestDataclass, **kwargs
    ) -> (int, Union[SuccessResponse, ErrorResponse],
          RenewTokenResponse):
        return await self._post(
            self.build_url(postfix_url=f'{id_}/cities/'),
            json=data.as_dict(),
            **kwargs)

    @expectations(schema=CitiesResponseSchema)
    async def cities(
        self, id_: int, **kwargs
    ) -> (int, Union[CitiesResponse, ErrorResponse],
          RenewTokenResponse):
        return await self._get(
            self.build_url(postfix_url=f'{id_}/cities/'),
            **kwargs)
