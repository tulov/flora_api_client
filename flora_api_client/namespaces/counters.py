from typing import Union

from flora_api_client.utils.decorators import expectations
from ..presentations.counters import CountersResponse
from ..schemas import ErrorResponseSchema, CountersResponseSchema
from ..namespaces.base import Namespace


class CountersNamespace(Namespace):
    URL = '/counters/'

    @expectations(schema=CountersResponseSchema)
    async def get(
        self, **kwargs
    ) -> (int, Union[CountersResponse, ErrorResponseSchema]):
        return await self._get(self.URL, **kwargs)
