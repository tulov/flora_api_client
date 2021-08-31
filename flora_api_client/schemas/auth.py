import marshmallow_dataclass
from flora_api_client.presentations.auth import (
    AuthRequest, AuthResponse
)


AuthRequestSchema = marshmallow_dataclass.class_schema(AuthRequest)
AuthResponseSchema = marshmallow_dataclass.class_schema(AuthResponse)
