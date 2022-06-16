from http import HTTPStatus
from typing import Union

from flora_api_client.utils.decorators import expectations
from ..presentations.auth import RenewTokenResponse
from ..presentations.slider import (
    SliderResponse, SliderItemRequest, SliderQuerystring, SliderItemResponse
)
from ..presentations.error import ErrorResponse
from ..schemas import SliderResponseSchema, SliderItemResponseSchema
from ..namespaces.base import Namespace


class SliderItemsNamespace(Namespace):
    URL = '/slider-items/'

    @expectations(schema=SliderResponseSchema)
    async def all(
        self, query_params: SliderQuerystring = None, **kwargs
    ) -> (int, Union[SliderResponse, ErrorResponse],
          RenewTokenResponse):
        return await self._get(self.build_url(query_params), **kwargs)

    @expectations(schema=SliderItemResponseSchema,
                  expected_code=HTTPStatus.CREATED)
    async def create(
        self, data: SliderItemRequest, **kwargs
    ) -> (int, Union[SliderItemResponse, ErrorResponse],
          RenewTokenResponse):
        return await self._post(self.URL, json=data.as_dict(), **kwargs)

    @expectations(schema=SliderItemResponseSchema)
    async def update(
        self, id_: int, data: SliderItemRequest, **kwargs
    ) -> (int, Union[SliderItemResponse, ErrorResponse],
          RenewTokenResponse):
        return await self._put(self.build_url(postfix_url=id_),
                               json=data.as_dict(), **kwargs)
