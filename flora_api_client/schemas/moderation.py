import marshmallow_dataclass
from flora_api_client.presentations.moderation import (
    RequestsForModerationResponse, RequestForModerationResponse,
    ModerationUpdateRequest
)


RequestsForModerationResponseSchema = marshmallow_dataclass.class_schema(
    RequestsForModerationResponse
)

RequestForModerationResponseSchema = marshmallow_dataclass.class_schema(
    RequestForModerationResponse
)

ModerationUpdateRequestSchema = marshmallow_dataclass.class_schema(
    ModerationUpdateRequest
)
