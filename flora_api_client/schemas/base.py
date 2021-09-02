import marshmallow_dataclass

from flora_api_client.presentations.base import SuccessResponse

SuccessResponseSchema = marshmallow_dataclass.class_schema(
    SuccessResponse
)
