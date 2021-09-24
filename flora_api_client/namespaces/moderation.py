from http import HTTPStatus
from typing import Union

from flora_api_client.utils.decorators import expectations
from ..presentations.auth import RenewTokenResponse
from ..presentations.moderation import (
    RequestsForModerationResponse, RequestForModerationResponse,
    ModerationUpdateRequest
)
from ..presentations.base import Querystring, WithFieldsQuerystring
from ..schemas import (
    RequestsForModerationResponseSchema, ErrorResponseSchema,
    RequestForModerationResponseSchema
)
from ..namespaces.base import Namespace


class ModerationNamespace(Namespace):
    URL = '/requests-for-moderation/'

    @expectations(schema=RequestsForModerationResponseSchema,
                  expected_code=HTTPStatus.OK)
    async def all(
        self, query_params: Querystring = None,  **kwargs
    ) -> (int, Union[RequestsForModerationResponse, ErrorResponseSchema],
          RenewTokenResponse):
        return await self._get(self.build_url(query_params), **kwargs)

    @expectations(schema=RequestForModerationResponseSchema,
                  expected_code=HTTPStatus.OK)
    async def get(
        self, id_: int, query_params: WithFieldsQuerystring = None, **kwargs
    ) -> (int, Union[RequestForModerationResponse, ErrorResponseSchema],
          RenewTokenResponse):
        return await self._get(
            self.build_url(query_params, postfix_url=id_), **kwargs)

    @expectations(schema=RequestForModerationResponseSchema,
                  expected_code=HTTPStatus.OK)
    async def update(
        self, id_: int, data: ModerationUpdateRequest, **kwargs
    ) -> (int, Union[RequestForModerationResponse, ErrorResponseSchema],
          RenewTokenResponse):
        return await self._put(
            self.build_url(postfix_url=id_), json=data.as_dict(), **kwargs)
