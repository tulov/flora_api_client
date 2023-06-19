from flora_api_client.utils.decorators import expectations
from ..namespaces.base import Namespace
from ..presentations.auth import RenewTokenResponse
from ..presentations.chats import ChatResponse
from ..presentations.error import ErrorResponse
from ..schemas.chats import ChatResponseSchema


class ChatsNamespace(Namespace):
    URL = "/chats/"

    @expectations(schema=ChatResponseSchema)
    async def url(
        self, order_id: int, **kwargs
    ) -> (int, ChatResponse | ErrorResponse, RenewTokenResponse):
        return await self._get(self.build_url(postfix_url=f"url/{order_id}"), **kwargs)
