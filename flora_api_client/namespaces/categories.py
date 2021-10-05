from http import HTTPStatus
from typing import Union

from flora_api_client.utils.decorators import expectations
from ..presentations.auth import RenewTokenResponse
from ..presentations.base import Querystring, WithFieldsQuerystring
from ..presentations.categories import (
    CategoryResponse, CreateCategoryRequest, CategoriesResponse
)
from ..presentations.tags import TagsResponse
from ..presentations.error import ErrorResponse
from ..schemas import (
    CategoryResponseSchema, CategoriesResponseSchema, TagsResponseSchema
)
from ..namespaces.base import Namespace


class CategoriesNamespace(Namespace):
    URL = '/categories/'

    @expectations(schema=CategoryResponseSchema,
                  expected_code=HTTPStatus.CREATED)
    async def create(
        self, data: CreateCategoryRequest, **kwargs
    ) -> (int, Union[CategoryResponse, ErrorResponse],
          RenewTokenResponse):
        return await self._post(self.URL, json=data.as_dict(), **kwargs)

    @expectations(schema=CategoryResponseSchema)
    async def update(
        self, id_: int, data: CreateCategoryRequest, **kwargs
    ) -> (int, Union[CategoryResponse, ErrorResponse],
          RenewTokenResponse):
        return await self._put(self.build_url(postfix_url=id_),
                               json=data.as_dict(), **kwargs)

    @expectations(schema=CategoriesResponseSchema)
    async def all(
        self, query_params: Querystring = None, **kwargs
    ) -> (int, Union[CategoriesResponse, ErrorResponse],
          RenewTokenResponse):
        return await self._get(self.build_url(query_params), **kwargs)

    @expectations(schema=CategoryResponseSchema)
    async def get(
        self, id_: int, query_params: WithFieldsQuerystring = None, **kwargs
    ) -> (int, Union[CategoryResponse, ErrorResponse],
          RenewTokenResponse):
        return await self._get(
            self.build_url(query_params, postfix_url=id_), **kwargs)

    @expectations(schema=TagsResponseSchema)
    async def tags(
        self, id_: int, query_params: WithFieldsQuerystring = None, **kwargs
    ) -> (int, Union[TagsResponse, ErrorResponse],
          RenewTokenResponse):
        return await self._get(
            self.build_url(query_params, postfix_url=f'{id_}/tags/'), **kwargs)
