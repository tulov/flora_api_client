import marshmallow_dataclass
from flora_api_client.presentations.auth import (
    AuthRequest, AuthResponse, RenewTokenRequest, RenewTokenResponse
)


AuthRequestSchema = marshmallow_dataclass.class_schema(AuthRequest)
AuthResponseSchema = marshmallow_dataclass.class_schema(AuthResponse)
RenewTokenRequestSchema = marshmallow_dataclass.class_schema(RenewTokenRequest)
RenewTokenResponseSchema = marshmallow_dataclass.class_schema(
    RenewTokenResponse
)
