from http import HTTPStatus
from typing import Union

from flora_api_client.utils.decorators import expectations
from ..presentations.auth import RenewTokenResponse
from ..presentations.base import (
    WithFieldsQuerystring, Querystring, ResultResponse
)
from ..presentations.orders import (
    OrderResponse, CreateOrderRequest, OrdersResponse, OrderCommentBase,
    OrderCommentResponse, OrderBillResponse, OrderBillRequest
)
from ..presentations.error import ErrorResponse
from ..schemas import (
    OrderResponseSchema, OrdersResponseSchema, OrderCommentResponseSchema,
    OrderBillResponseSchema, ResultResponseSchema
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

    @expectations(schema=OrdersResponseSchema)
    async def all(
        self, query_params: Querystring = None, **kwargs
    ) -> (int, Union[OrdersResponse, ErrorResponse],
          RenewTokenResponse):
        return await self._get(self.build_url(query_params), **kwargs)

    @expectations(schema=OrderCommentResponseSchema,
                  expected_code=HTTPStatus.CREATED)
    async def comment(
        self, order_id: int, data: OrderCommentBase, **kwargs
    ) -> (int, Union[OrderCommentResponse, ErrorResponse],
          RenewTokenResponse):
        return await self._post(
            self.build_url(postfix_url=f"{order_id}/comments/"),
            json=data.as_dict(), **kwargs)

    @expectations(schema=OrderBillResponseSchema,
                  expected_code=HTTPStatus.CREATED)
    async def bill(
        self, order_id: int, data: OrderBillRequest, **kwargs
    ) -> (int, Union[OrderBillResponse, ErrorResponse],
          RenewTokenResponse):
        return await self._post(
            self.build_url(postfix_url=f"{order_id}/bills/"),
            json=data.as_dict(), **kwargs)

    @expectations(schema=ResultResponseSchema)
    async def accept(
        self, order_id: int, **kwargs
    ) -> (int, Union[ResultResponse, ErrorResponse],
          RenewTokenResponse):
        return await self._put(
            self.build_url(postfix_url=f"{order_id}/accept/"), **kwargs)
