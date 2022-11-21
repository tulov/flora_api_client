from http import HTTPStatus
from typing import Union

from flora_api_client.utils.decorators import expectations
from ..presentations.auth import RenewTokenResponse
from ..presentations.images import (
    ImageResponse, ImageUploadRequest
)
from ..presentations.base import SuccessResponse
from ..presentations.error import ErrorResponse
from ..schemas import ImageResponseSchema, SuccessResponseSchema
from ..namespaces.base import Namespace


class ImagesNamespace(Namespace):
    URL = '/images/'

    @expectations(schema=ImageResponseSchema,
                  expected_code=HTTPStatus.CREATED)
    async def upload(
        self, data: ImageUploadRequest, **kwargs
    ) -> (int, Union[ImageResponse, ErrorResponse],
          RenewTokenResponse):
        return await self._post(self.URL, json=data.as_dict(), **kwargs)

    @expectations(schema=SuccessResponseSchema)
    async def unbind(
        self, id_: int, **kwargs
    ) -> (int, Union[SuccessResponse, ErrorResponse],
          RenewTokenResponse):
        return await self._put(
            self.build_url(postfix_url=f"{id_}"), json={}, **kwargs)
