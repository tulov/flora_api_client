import marshmallow_dataclass
from flora_api_client.presentations.auth import (
    AuthRequest
)


AuthRequestSchema = marshmallow_dataclass.class_schema(AuthRequest)
