from flora_api_client.utils.decorators import expectations
from ..namespaces.base import Namespace
from ..presentations.auth import RenewTokenResponse
from ..presentations.base import ResultResponse
from ..presentations.chats import ChatResponse
from ..presentations.error import ErrorResponse
from ..schemas import ResultResponseSchema
from ..schemas.chats import ChatResponseSchema


class ChatsNamespace(Namespace):
    URL = "/chats/"

    @expectations(schema=ChatResponseSchema)
    async def url(
        self, **kwargs
    ) -> (int, ChatResponse | ErrorResponse, RenewTokenResponse):
        return await self._get(self.build_url(postfix_url="url/"), **kwargs)

    @expectations(schema=ResultResponseSchema)
    async def users(
        self, order_id, **kwargs
    ) -> (int, ResultResponse | ErrorResponse, RenewTokenResponse):
        return await self._get(
            self.build_url(postfix_url=f"order/{order_id}/users/"), **kwargs
        )
