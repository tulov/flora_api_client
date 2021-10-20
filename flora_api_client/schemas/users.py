import marshmallow_dataclass
from flora_api_client.presentations.users import (
    DataForAuth, User, RegistrationUserData, ConfirmDataForAuthRequest,
    UsersResponse, ChangePasswordRequest
)
from ..presentations.base import SuccessResponse
from ..presentations.partners import BindCityRequestDataclass


DataForAuthSchema = marshmallow_dataclass.class_schema(DataForAuth)
UserSchema = marshmallow_dataclass.class_schema(User)
RegistrationUserSchema = marshmallow_dataclass.class_schema(
    RegistrationUserData
)
ConfirmDataForAuthRequestSchema = marshmallow_dataclass.class_schema(
    ConfirmDataForAuthRequest
)
ConfirmDataForAuthResponseSchema = marshmallow_dataclass.class_schema(
    SuccessResponse
)
UsersResponseSchema = marshmallow_dataclass.class_schema(
    UsersResponse
)
ChangePasswordRequestSchema = marshmallow_dataclass.class_schema(
    ChangePasswordRequest
)

BindCityRequestSchema = marshmallow_dataclass.class_schema(
    BindCityRequestDataclass
)
