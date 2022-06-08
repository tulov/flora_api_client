import marshmallow_dataclass
from flora_api_client.presentations.menu import (
    MenuRequest, MenuResponse
)


MenuResponseSchema = marshmallow_dataclass.class_schema(
    MenuResponse
)

MenuRequestSchema = marshmallow_dataclass.class_schema(
    MenuRequest
)
