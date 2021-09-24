from typing import Union

from flora_api_client.utils.decorators import expectations
from ..presentations.auth import RenewTokenResponse
from ..presentations.main import ApplicationInfoResponse
from ..schemas import ErrorResponseSchema, ApplicationInfoResponseSchema
from ..namespaces.base import Namespace


class InfoNamespace(Namespace):
    URL = '/info/'

    @expectations(schema=ApplicationInfoResponseSchema)
    async def get(
        self, **kwargs
    ) -> (int, Union[ApplicationInfoResponse, ErrorResponseSchema],
          RenewTokenResponse):
        return await self._get(self.URL, **kwargs)
