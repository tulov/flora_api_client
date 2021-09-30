import marshmallow_dataclass
from flora_api_client.presentations.categories import (
    CategoryResponse, CreateCategoryRequest, CategoriesResponse
)


CategoryResponseSchema = marshmallow_dataclass.class_schema(
    CategoryResponse
)
CategoriesResponseSchema = marshmallow_dataclass.class_schema(
    CategoriesResponse
)
CreateCategoryRequestSchema = marshmallow_dataclass.class_schema(
    CreateCategoryRequest
)
