import marshmallow_dataclass
from flora_api_client.presentations.prices import (
    PriceResponse, PricesResponse, PricesRequest
)
from marshmallow import Schema, EXCLUDE

Schema.Meta.unknown = EXCLUDE


PriceResponseSchema = marshmallow_dataclass.class_schema(
    PriceResponse
)
PricesResponseSchema = marshmallow_dataclass.class_schema(
    PricesResponse
)
PricesRequestSchema = marshmallow_dataclass.class_schema(
    PricesRequest
)
