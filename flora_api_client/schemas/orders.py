import marshmallow_dataclass
from flora_api_client.presentations.orders import (
    CreateOrderRequest, OrderResponse, OrdersResponse, OrderCommentBase,
    OrderCommentResponse, OrderBillResponse, OrderBillRequest
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
OrderCommentRequestSchema = marshmallow_dataclass.class_schema(
    OrderCommentBase
)
OrderCommentResponseSchema = marshmallow_dataclass.class_schema(
    OrderCommentResponse
)
OrderBillResponseSchema = marshmallow_dataclass.class_schema(
    OrderBillResponse
)
OrderBillRequestSchema = marshmallow_dataclass.class_schema(
    OrderBillRequest
)
