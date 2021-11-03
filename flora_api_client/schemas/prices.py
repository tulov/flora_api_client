import marshmallow_dataclass
from flora_api_client.presentations.prices import (
    PriceResponse, PricesResponse
)


PriceResponseSchema = marshmallow_dataclass.class_schema(
    PriceResponse
)
PricesResponseSchema = marshmallow_dataclass.class_schema(
    PricesResponse
)
