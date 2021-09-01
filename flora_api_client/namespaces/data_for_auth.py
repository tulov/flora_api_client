from http import HTTPStatus
from typing import Union

from flora_api_client.utils.decorators import expectations
from ..presentations.users import (
    ConfirmDataForAuthResponse, ConfirmDataForAuthRequest
)
from ..schemas import ConfirmDataForAuthResponseSchema, ErrorResponseSchema
from ..namespaces.base import Namespace


class DataForAuthNamespace(Namespace):
    URL = '/data_for_auth/'

    @expectations(schema=ConfirmDataForAuthResponseSchema,
                  expected_code=HTTPStatus.OK)
    async def confirm(
        self, data_id: int, data: ConfirmDataForAuthRequest
    ) -> (int, Union[ConfirmDataForAuthResponse, ErrorResponseSchema]):
        return await self._put(f'{self.URL}{data_id}/confirm/',
                               json=data.as_dict())
