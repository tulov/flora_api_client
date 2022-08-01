from http import HTTPStatus
from typing import Union

from flora_api_client.utils.decorators import expectations
from ..presentations.auth import RenewTokenResponse
from ..presentations.base import WithFieldsQuerystring
from ..presentations.orders import (
    OrderResponse, CreateOrderRequest
)
from ..presentations.error import ErrorResponse
from ..schemas import (
    OrderResponseSchema
)
from ..namespaces.base import Namespace


class OrdersNamespace(Namespace):
    URL = '/orders/'

    @expectations(schema=OrderResponseSchema,
                  expected_code=HTTPStatus.CREATED)
    async def create(
        self, data: CreateOrderRequest, **kwargs
    ) -> (int, Union[OrderResponse, ErrorResponse],
          RenewTokenResponse):
        return await self._post(self.URL, json=data.as_dict(), **kwargs)

    @expectations(schema=OrderResponseSchema)
    async def get(
        self, id_: int, query_params: WithFieldsQuerystring = None, **kwargs
    ) -> (int, Union[OrderResponse, ErrorResponse],
          RenewTokenResponse):
        return await self._get(
            self.build_url(query_params, postfix_url=id_), **kwargs)

