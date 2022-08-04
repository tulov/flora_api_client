from typing import Union

from flora_api_client.utils.decorators import expectations
from ..presentations.auth import RenewTokenResponse
from ..presentations.base import WithFieldsQuerystring, Querystring
from ..presentations.bills import (
    BillsResponse, BillResponse
)
from ..presentations.error import ErrorResponse
from ..schemas import (
    BillsResponseSchema, BillResponseSchema
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
