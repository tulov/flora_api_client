import marshmallow_dataclass
from flora_api_client.presentations.bills import (
    BillsResponse, BillResponse
)


BillResponseSchema = marshmallow_dataclass.class_schema(
    BillResponse
)
BillsResponseSchema = marshmallow_dataclass.class_schema(
    BillsResponse
)
