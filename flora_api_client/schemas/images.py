import marshmallow_dataclass
from flora_api_client.presentations.images import (
    ImageResponse, ImageUploadRequest
)


ImageResponseSchema = marshmallow_dataclass.class_schema(
    ImageResponse
)
ImageUploadRequestSchema = marshmallow_dataclass.class_schema(
    ImageUploadRequest
)
