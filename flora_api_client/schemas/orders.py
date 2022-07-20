import marshmallow_dataclass
from flora_api_client.presentations.orders import (
    CreateOrderRequest, OrderResponse
)


CreateOrderRequestSchema = marshmallow_dataclass.class_schema(
    CreateOrderRequest
)
OrderResponseSchema = marshmallow_dataclass.class_schema(
    OrderResponse
)
