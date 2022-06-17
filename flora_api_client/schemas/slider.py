import marshmallow_dataclass
from flora_api_client.presentations.slider import (
    SliderItemRequest, SliderResponse, SliderItemResponse
)


SliderResponseSchema = marshmallow_dataclass.class_schema(
    SliderResponse
)

SliderItemRequestSchema = marshmallow_dataclass.class_schema(
    SliderItemRequest
)

SliderItemResponseSchema = marshmallow_dataclass.class_schema(
    SliderItemResponse
)
