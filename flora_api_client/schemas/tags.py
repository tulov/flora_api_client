import marshmallow_dataclass
from flora_api_client.presentations.tags import (
    TagResponse, CreateTagRequest, TagsResponse
)


TagResponseSchema = marshmallow_dataclass.class_schema(
    TagResponse
)
TagsResponseSchema = marshmallow_dataclass.class_schema(
    TagsResponse
)
CreateTagRequestSchema = marshmallow_dataclass.class_schema(
    CreateTagRequest
)
