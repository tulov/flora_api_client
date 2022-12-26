import marshmallow_dataclass
from flora_api_client.presentations.menu import (
    MenuRequest, MenuResponse, MenuQuerystring, Menu
)
from marshmallow import Schema, EXCLUDE

Schema.Meta.unknown = EXCLUDE


MenuResponseSchema = marshmallow_dataclass.class_schema(
    MenuResponse
)

MenuRequestSchema = marshmallow_dataclass.class_schema(
    MenuRequest
)

MenuQuerystringSchema = marshmallow_dataclass.class_schema(
    MenuQuerystring
)
MenuSchema = marshmallow_dataclass.class_schema(
    Menu
)
