from flora_api_client.utils.decorators import expectations
from ..namespaces.base import Namespace
from ..presentations.auth import RenewTokenResponse
from ..presentations.error import ErrorResponse
from ..presentations.main_page import MainPage, MainPageResponse
from ..schemas.main_page import MainPageResponseSchema


class MainPageNamespace(Namespace):
    URL = "/main-page/"

    @expectations(schema=MainPageResponseSchema)
    async def get(
        self, **kwargs
    ) -> (int, MainPageResponse | ErrorResponse, RenewTokenResponse):
        return await self._get(self.build_url(), **kwargs)

    @expectations(schema=MainPageResponseSchema)
    async def update(
        self, data: MainPage, **kwargs
    ) -> (int, MainPageResponse | ErrorResponse, RenewTokenResponse):
        return await self._put(self.build_url(), json=data.as_dict(), **kwargs)
