import marshmallow_dataclass
from flora_api_client.presentations.users import (
    DataForAuth, User, RegistrationUserData
)


DataForAuthSchema = marshmallow_dataclass.class_schema(DataForAuth)
UserSchema = marshmallow_dataclass.class_schema(User)
RegistrationUserSchema = marshmallow_dataclass.class_schema(
    RegistrationUserData
)
