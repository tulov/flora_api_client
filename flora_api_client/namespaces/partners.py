from http import HTTPStatus
from typing import Union

from flora_api_client.utils.decorators import expectations
from ..presentations.auth import RenewTokenResponse
from ..presentations.error import ErrorResponse
from ..presentations.users import RegistrationUserData, User
from ..presentations.partners import BindCityRequestDataclass
from ..presentations.base import SuccessResponse, Querystring
from ..presentations.cities import CitiesResponse, CityResponse
from ..schemas import (
    UserSchema, SuccessResponseSchema, CitiesResponseSchema, CityResponseSchema
)
from ..namespaces.base import Namespace


class PartnersNamespace(Namespace):
    URL = '/partners/'

    @expectations(schema=UserSchema,
                  expected_code=HTTPStatus.CREATED)
    async def register(
        self, data: RegistrationUserData, **kwargs
    ) -> (int, Union[User, ErrorResponse], RenewTokenResponse):
        return await self._post(self.URL, json=data.as_dict(), **kwargs)

    @expectations(schema=CityResponseSchema,
                  expected_code=HTTPStatus.CREATED)
    async def bind_city(
        self, id_: int, data: BindCityRequestDataclass, **kwargs
    ) -> (int, Union[CityResponse, ErrorResponse],
          RenewTokenResponse):
        return await self._post(
            self.build_url(postfix_url=f'{id_}/cities/'),
            json=data.as_dict(),
            **kwargs)

    @expectations(schema=CitiesResponseSchema)
    async def cities(
        self, id_: int, query_params: Querystring = None, **kwargs
    ) -> (int, Union[CitiesResponse, ErrorResponse],
          RenewTokenResponse):
        return await self._get(
            self.build_url(query_params, postfix_url=f'{id_}/cities/'),
            **kwargs)

    @expectations(schema=CityResponseSchema)
    async def city_detail(
        self, id_: int, geoname_id: int,
        query_params: Querystring = None, **kwargs
    ) -> (int, Union[CityResponse, ErrorResponse],
          RenewTokenResponse):
        return await self._get(
            self.build_url(query_params,
                           postfix_url=f'{id_}/cities/{geoname_id}'),
            **kwargs)

    @expectations(schema=CityResponseSchema)
    async def update_city(
        self, id_: int, data: BindCityRequestDataclass, **kwargs
    ) -> (int, Union[CityResponse, ErrorResponse],
          RenewTokenResponse):
        return await self._put(
            self.build_url(postfix_url=f'{id_}/cities/{data.geoname_id}'),
            json=data.as_dict(),
            **kwargs)

    @expectations(schema=SuccessResponseSchema)
    async def delete_city(
        self, id_: int, geoname_id: int, **kwargs
    ) -> (int, Union[SuccessResponse, ErrorResponse],
          RenewTokenResponse):
        return await self._delete(
            self.build_url(postfix_url=f'{id_}/cities/{geoname_id}'),
            **kwargs)
