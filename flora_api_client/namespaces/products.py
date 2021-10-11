from http import HTTPStatus
from typing import Union

from flora_api_client.utils.decorators import expectations
from ..presentations.auth import RenewTokenResponse
from ..presentations.base import Querystring
from ..presentations.products import (
    ProductResponse, ProductRequest, ProductsResponse
)
from ..presentations.error import ErrorResponse
from ..schemas import ProductResponseSchema, ProductsResponseSchema
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

    @expectations(schema=ProductsResponseSchema)
    async def all(
        self, query_params: Querystring = None, **kwargs
    ) -> (int, Union[ProductsResponse, ErrorResponse],
          RenewTokenResponse):
        return await self._get(self.build_url(query_params), **kwargs)
