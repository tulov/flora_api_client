from typing import Union

from flora_api_client.utils.decorators import expectations
from ..presentations.auth import RenewTokenResponse
from ..presentations.menu import (
    MenuResponse, MenuRequest
)
from ..presentations.error import ErrorResponse
from ..schemas import MenuResponseSchema
from ..namespaces.base import Namespace


class MenuNamespace(Namespace):
    URL = '/menu/'

    @expectations(schema=MenuResponseSchema)
    async def all(
        self, **kwargs
    ) -> (int, Union[MenuResponse, ErrorResponse],
          RenewTokenResponse):
        return await self._get(self.build_url(), **kwargs)

    @expectations(schema=MenuResponseSchema)
    async def apply(
        self, data: MenuRequest, **kwargs
    ) -> (int, Union[MenuResponse, ErrorResponse],
          RenewTokenResponse):
        return await self._put(self.build_url(),
                               json=data.as_dict(), **kwargs)
