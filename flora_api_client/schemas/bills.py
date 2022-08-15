import marshmallow_dataclass
from marshmallow import Schema, EXCLUDE
from flora_api_client.presentations.bills import (
    BillsResponse, BillResponse, BillPayRequest, CloudpaymentsBillPayRequest,
    CloudpaymentsBillAfter3dRequest
)

Schema.Meta.unknown = EXCLUDE


BillResponseSchema = marshmallow_dataclass.class_schema(
    BillResponse
)
BillsResponseSchema = marshmallow_dataclass.class_schema(
    BillsResponse
)
BillPayRequestSchema = marshmallow_dataclass.class_schema(
    BillPayRequest
)
CloudpaymentsBillPayRequestSchema = marshmallow_dataclass.class_schema(
    CloudpaymentsBillPayRequest
)
CloudpaymentsBillAfter3dRequestSchema = marshmallow_dataclass.class_schema(
    CloudpaymentsBillAfter3dRequest
)
