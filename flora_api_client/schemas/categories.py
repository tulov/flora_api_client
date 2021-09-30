import marshmallow_dataclass
from flora_api_client.presentations.categories import CategoryResponse


CategoryResponseSchema = marshmallow_dataclass.class_schema(
    CategoryResponse
)
