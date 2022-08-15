import marshmallow_dataclass
from flora_api_client.presentations.orders import (
    CreateOrderRequest, OrderResponse, OrdersResponse
)
from marshmallow import Schema, EXCLUDE

Schema.Meta.unknown = EXCLUDE


CreateOrderRequestSchema = marshmallow_dataclass.class_schema(
    CreateOrderRequest
)
OrderResponseSchema = marshmallow_dataclass.class_schema(
    OrderResponse
)
OrdersResponseSchema = marshmallow_dataclass.class_schema(
    OrdersResponse
)
