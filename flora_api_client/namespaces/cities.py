from typing import Union

from flora_api_client.utils.decorators import expectations
from ..presentations.auth import RenewTokenResponse
from ..presentations.base import Querystring
from ..presentations.cities import (
    CitiesResponse
)
from ..presentations.error import ErrorResponse
from ..schemas import CitiesResponseSchema
from ..namespaces.base import Namespace


class CitiesNamespace(Namespace):
    URL = '/cities/'

    @expectations(schema=CitiesResponseSchema)
    async def all(
        self, query_params: Querystring = None, **kwargs
    ) -> (int, Union[CitiesResponse, ErrorResponse],
          RenewTokenResponse):
        return await self._get(self.build_url(query_params), **kwargs)
