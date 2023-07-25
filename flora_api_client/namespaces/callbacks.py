from http import HTTPStatus

from flora_api_client.utils.decorators import expectations
from ..namespaces.base import Namespace
from ..presentations.auth import RenewTokenResponse
from ..presentations.base import Querystring, SuccessResponse
from ..presentations.error import ErrorResponse
from ..presentations.callbacks import Callback, CallbackResponse, CallbacksResponse
from ..schemas.callbacks import CallbackResponseSchema, CallbacksResponseSchema
from ..schemas import SuccessResponseSchema


class CallbacksNamespace(Namespace):
    URL = "/callbacks/"

    @expectations(schema=CallbackResponseSchema, expected_code=HTTPStatus.CREATED)
    async def create(
        self, data: Callback, **kwargs
    ) -> (int, CallbackResponse | ErrorResponse, RenewTokenResponse):
        return await self._post(self.URL, json=data.as_dict(), **kwargs)

    @expectations(schema=CallbacksResponseSchema)
    async def all(
        self, query_params: Querystring = None, **kwargs
    ) -> (int, CallbacksResponse | ErrorResponse, RenewTokenResponse):
        return await self._get(self.build_url(query_params), **kwargs)

    @expectations(schema=CallbackResponseSchema)
    async def update(
        self, id_: int, body: Callback, **kwargs
    ) -> (int, CallbackResponse | ErrorResponse, RenewTokenResponse):
        return await self._put(self.build_url(postfix_url=id_), **kwargs)

    @expectations(schema=SuccessResponseSchema)
    async def remove(
        self, id_: int, **kwargs
    ) -> (int, SuccessResponse | ErrorResponse, RenewTokenResponse):
        return await self._delete(self.build_url(postfix_url=id_), **kwargs)
