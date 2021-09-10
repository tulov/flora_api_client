import marshmallow_dataclass

from flora_api_client.presentations.base import (
    SuccessResponse, Querystring, WithFieldsQuerystring
)

SuccessResponseSchema = marshmallow_dataclass.class_schema(
    SuccessResponse
)

QuerystringSchema = marshmallow_dataclass.class_schema(
    Querystring
)

WithFieldsQuerystringSchema = marshmallow_dataclass.class_schema(
    WithFieldsQuerystring
)
