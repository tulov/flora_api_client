from http import HTTPStatus
from typing import Union

from flora_api_client.utils.decorators import expectations
from ..presentations.moderation import (
    RequestsForModerationResponse, RequestForModerationResponse
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
    ) -> (int, Union[RequestsForModerationResponse, ErrorResponseSchema]):
        return await self._get(self.build_url(query_params), **kwargs)

    @expectations(schema=RequestForModerationResponseSchema,
                  expected_code=HTTPStatus.OK)
    async def get(
        self, id_: int, query_params: WithFieldsQuerystring = None, **kwargs
    ) -> (int, Union[RequestForModerationResponse, ErrorResponseSchema]):
        return await self._get(
            self.build_url(query_params, postfix_url=id_), **kwargs)
