from http import HTTPStatus
from typing import Union

from flora_api_client.utils.decorators import expectations
from ..presentations.auth import RenewTokenResponse
from ..presentations.base import Querystring, WithFieldsQuerystring
from ..presentations.products import (
    ProductResponse, ProductRequest, ProductsResponse, FeaturedProductsResponse,
    FeaturedProductsQuerystring, PreferredExecutorResponse,
    PreferredExecutorQuerystring
)
from ..presentations.error import ErrorResponse
from ..schemas import (
    ProductResponseSchema, ProductsResponseSchema,
    FeaturedProductsResponseSchema, PreferredExecutorResponseSchema
)
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

    @expectations(schema=ProductResponseSchema)
    async def get(
        self, id_: int, query_params: WithFieldsQuerystring = None, **kwargs
    ) -> (int, Union[ProductResponse, ErrorResponse],
          RenewTokenResponse):
        return await self._get(
            self.build_url(query_params, postfix_url=id_), **kwargs)

    @expectations(schema=ProductResponseSchema)
    async def update(
        self, id_: int, data: ProductRequest, **kwargs
    ) -> (int, Union[ProductResponse, ErrorResponse],
          RenewTokenResponse):
        return await self._put(self.build_url(postfix_url=id_),
                               json=data.as_dict(), **kwargs)

    @expectations(schema=FeaturedProductsResponseSchema)
    async def featured(
        self, city_id: int, category: Union[int, str],
        query_params: FeaturedProductsQuerystring = None, **kwargs
    ) -> (int, Union[FeaturedProductsResponse, ErrorResponse],
          RenewTokenResponse):
        postfix_url = 'featured/{}/{}'.format(city_id, category)
        return await self._get(self.build_url(query_params,
                                              postfix_url=postfix_url),
                               **kwargs)

    @expectations(schema=PreferredExecutorResponseSchema)
    async def preferred_executor(
        self, id_: int, city_id: int,
        query_params: PreferredExecutorQuerystring = None, **kwargs
    ) -> (int, Union[PreferredExecutorResponse, ErrorResponse],
          RenewTokenResponse):
        postfix_url = '{}/preferred-executor/{}'.format(id_, city_id)
        return await self._get(self.build_url(query_params,
                                              postfix_url=postfix_url),
                               **kwargs)


