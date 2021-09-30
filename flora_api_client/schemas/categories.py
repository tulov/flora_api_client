import marshmallow_dataclass
from flora_api_client.presentations.categories import (
    CategoryResponse, CreateCategoryRequest
)


CategoryResponseSchema = marshmallow_dataclass.class_schema(
    CategoryResponse
)
CreateCategoryRequestSchema = marshmallow_dataclass.class_schema(
    CreateCategoryRequest
)
