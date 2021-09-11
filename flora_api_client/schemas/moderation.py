import marshmallow_dataclass
from flora_api_client.presentations.moderation import (
    RequestsForModerationResponse, RequestForModerationResponse,
    ModerationResult
)


RequestsForModerationResponseSchema = marshmallow_dataclass.class_schema(
    RequestsForModerationResponse
)

RequestForModerationResponseSchema = marshmallow_dataclass.class_schema(
    RequestForModerationResponse
)

ModerateResultSchema = marshmallow_dataclass.class_schema(
    ModerationResult
)
