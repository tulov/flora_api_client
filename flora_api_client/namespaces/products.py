from http import HTTPStatus
from typing import Union

from flora_api_client.utils.decorators import expectations
from ..presentations.auth import RenewTokenResponse
from ..presentations.products import (
    ProductResponse, ProductRequest
)
from ..presentations.error import ErrorResponse
from ..schemas import ProductResponseSchema
from ..namespaces.base import Namespace


class ProductsNamespace(Namespace):
    URL = '/products/'

    @expectations(schema=ProductResponseSchema,
                  expected_code=HTTPStatus.CREATED)
    async def create(
        self, data: ProductRequest, **kwargs
    ) -> (int, Union[ProductResponse, ErrorResponse],
          RenewTokenResponse):
        return await self._post(self.URL, json=data.as_dict(), **kwargs)

