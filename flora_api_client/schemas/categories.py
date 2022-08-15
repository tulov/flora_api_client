import marshmallow_dataclass
from flora_api_client.presentations.categories import (
    CategoryResponse, CreateCategoryRequest, CategoriesResponse,
    FilterCounterRequest, FilterCounterResponse
)
from marshmallow import Schema, EXCLUDE

Schema.Meta.unknown = EXCLUDE


CategoryResponseSchema = marshmallow_dataclass.class_schema(
    CategoryResponse
)
CategoriesResponseSchema = marshmallow_dataclass.class_schema(
    CategoriesResponse
)
CreateCategoryRequestSchema = marshmallow_dataclass.class_schema(
    CreateCategoryRequest
)
FilterCounterRequestSchema = marshmallow_dataclass.class_schema(
    FilterCounterRequest
)

FilterCounterResponseSchema = marshmallow_dataclass.class_schema(
    FilterCounterResponse
)
