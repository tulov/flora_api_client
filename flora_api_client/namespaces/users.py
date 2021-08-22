from http import HTTPStatus
from typing import Union

from flora_api_client.utils.decorators import expectations
from ..presentations.users import RegistrationUserData, User
from ..schemas import UserSchema, ErrorResponseSchema
from ..namespaces.base import Namespace


class UsersNamespace(Namespace):
    URL = '/users/'

    @expectations(schema=UserSchema,
                  expected_code=HTTPStatus.CREATED)
    async def register(
        self, data: RegistrationUserData
    ) -> (int, Union[User, ErrorResponseSchema]):
        return await self._post(self.URL, json=data.as_dict())
