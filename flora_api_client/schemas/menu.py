import marshmallow_dataclass
from flora_api_client.presentations.menu import (
    MenuItemRequest, MenuResponse, MenuItemResponse
)


MenuResponseSchema = marshmallow_dataclass.class_schema(
    MenuResponse
)

MenuItemResponseSchema = marshmallow_dataclass.class_schema(
    MenuItemResponse
)

MenuItemRequestSchema = marshmallow_dataclass.class_schema(
    MenuItemRequest
)
