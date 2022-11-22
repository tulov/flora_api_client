from http import HTTPStatus
from typing import Union

from flora_api_client.utils.decorators import expectations
from ..presentations.auth import RenewTokenResponse
from ..presentations.images import (
    ImageResponse, ImageUploadRequest
)
from ..presentations.error import ErrorResponse
from ..schemas import ImageResponseSchema
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
