from typing import Union

from flora_api_client.utils.decorators import expectations
from ..presentations.auth import RenewTokenResponse
from ..presentations.base import WithFieldsQuerystring, Querystring
from ..presentations.bills import (
    BillsResponse, BillResponse, BillPayRequest
)
from ..presentations.error import ErrorResponse
from ..schemas import (
    BillsResponseSchema, BillResponseSchema, SuccessResponseSchema
)
from ..namespaces.base import Namespace


class BillsNamespace(Namespace):
    URL = '/bills/'

    @expectations(schema=BillResponseSchema)
    async def get(
        self, guid: str, query_params: WithFieldsQuerystring = None, **kwargs
    ) -> (int, Union[BillResponse, ErrorResponse],
          RenewTokenResponse):
        return await self._get(
            self.build_url(query_params, postfix_url=guid), **kwargs)

    @expectations(schema=BillsResponseSchema)
    async def all(
        self, query_params: Querystring = None, **kwargs
    ) -> (int, Union[BillsResponse, ErrorResponse],
          RenewTokenResponse):
        return await self._get(self.build_url(query_params), **kwargs)

    @expectations(schema=SuccessResponseSchema)
    async def pay(
        self, guid: str, pay_service: str, data: BillPayRequest, **kwargs
    ) -> (int, Union[BillsResponse, ErrorResponse],
          RenewTokenResponse):
        return await self._post(
            self.build_url(postfix_url=f"{guid}/pay/{pay_service}"),
            json=data.as_dict(), **kwargs)
