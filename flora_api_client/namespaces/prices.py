from typing import Union

from flora_api_client.utils.decorators import expectations
from ..presentations.auth import RenewTokenResponse
from ..presentations.base import Querystring
from ..presentations.prices import (
    PricesResponse
)
from ..presentations.error import ErrorResponse
from ..schemas import PricesResponseSchema
from ..namespaces.base import Namespace


class PricesNamespace(Namespace):
    URL = '/prices/'

    @expectations(schema=PricesResponseSchema)
    async def all(
        self, query_params: Querystring = None, **kwargs
    ) -> (int, Union[PricesResponse, ErrorResponse],
          RenewTokenResponse):
        return await self._get(self.build_url(query_params), **kwargs)
