from http import HTTPStatus
from typing import Union

from flora_api_client.utils.decorators import expectations
from ..presentations.auth import RenewTokenResponse
from ..presentations.error import ErrorResponse
from ..presentations.users import RegistrationUserData, User
from ..schemas import UserSchema
from ..namespaces.base import Namespace


class PartnersNamespace(Namespace):
    URL = '/partners/'

    @expectations(schema=UserSchema,
                  expected_code=HTTPStatus.CREATED)
    async def register(
        self, data: RegistrationUserData, **kwargs
    ) -> (int, Union[User, ErrorResponse], RenewTokenResponse):
        return await self._post(self.URL, json=data.as_dict(), **kwargs)
