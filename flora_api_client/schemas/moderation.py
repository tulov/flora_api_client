import marshmallow_dataclass
from flora_api_client.presentations.moderation import (
    RequestsForModerationResponse
)


RequestForModerationResponseSchema = marshmallow_dataclass.class_schema(
    RequestsForModerationResponse
)
