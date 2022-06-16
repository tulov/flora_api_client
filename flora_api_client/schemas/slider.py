import marshmallow_dataclass
from flora_api_client.presentations.slider import (
    SliderItemRequest, SliderResponse, SliderQuerystring, SliderItemResponse
)


SliderResponseSchema = marshmallow_dataclass.class_schema(
    SliderResponse
)

SliderItemRequestSchema = marshmallow_dataclass.class_schema(
    SliderItemRequest
)

SliderQuerystringSchema = marshmallow_dataclass.class_schema(
    SliderQuerystring
)

SliderItemResponseSchema = marshmallow_dataclass.class_schema(
    SliderItemResponse
)
