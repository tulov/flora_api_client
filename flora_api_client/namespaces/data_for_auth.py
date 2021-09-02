from http import HTTPStatus
from typing import Union

from flora_api_client.utils.decorators import expectations
from ..presentations.users import (
    ConfirmDataForAuthRequest
)
from ..presentations.base import SuccessResponse
from ..schemas import SuccessResponseSchema, ErrorResponseSchema
from ..namespaces.base import Namespace


class DataForAuthNamespace(Namespace):
    URL = '/data_for_auth/'

    @expectations(schema=SuccessResponseSchema,
                  expected_code=HTTPStatus.OK)
    async def confirm(
        self, data_id: int, data: ConfirmDataForAuthRequest
    ) -> (int, Union[SuccessResponse, ErrorResponseSchema]):
        return await self._put(f'{self.URL}{data_id}/confirm/',
                               json=data.as_dict())

    @expectations(schema=SuccessResponseSchema,
                  expected_code=HTTPStatus.OK)
    async def resend(self, data_id: int
                     ) -> (int, Union[SuccessResponse, ErrorResponseSchema]):
        return await self._put(f'{self.URL}{data_id}/send/')
