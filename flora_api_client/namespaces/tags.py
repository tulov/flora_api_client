from http import HTTPStatus
from typing import Union

from flora_api_client.utils.decorators import expectations
from ..presentations.auth import RenewTokenResponse
from ..presentations.base import Querystring, WithFieldsQuerystring
from ..presentations.tags import (
    TagResponse, CreateTagRequest, TagsResponse
)
from ..presentations.error import ErrorResponse
from ..schemas import TagResponseSchema, TagsResponseSchema
from ..namespaces.base import Namespace


class TagsNamespace(Namespace):
    URL = '/tags/'

    @expectations(schema=TagResponseSchema,
                  expected_code=HTTPStatus.CREATED)
    async def create(
        self, data: CreateTagRequest, **kwargs
    ) -> (int, Union[TagResponse, ErrorResponse],
          RenewTokenResponse):
        return await self._post(self.URL, json=data.as_dict(), **kwargs)

    @expectations(schema=TagsResponseSchema)
    async def all(
        self, query_params: Querystring = None, **kwargs
    ) -> (int, Union[TagsResponse, ErrorResponse],
          RenewTokenResponse):
        return await self._get(self.build_url(query_params), **kwargs)

    @expectations(schema=TagResponseSchema)
    async def get(
        self, id_: int, query_params: WithFieldsQuerystring = None, **kwargs
    ) -> (int, Union[TagResponse, ErrorResponse],
          RenewTokenResponse):
        return await self._get(
            self.build_url(query_params, postfix_url=id_), **kwargs)


