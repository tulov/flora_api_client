import marshmallow_dataclass
from flora_api_client.presentations.fields import (
    FieldResponse, CreateFieldRequest, FieldsResponse
)


FieldResponseSchema = marshmallow_dataclass.class_schema(
    FieldResponse
)
FieldsResponseSchema = marshmallow_dataclass.class_schema(
    FieldsResponse
)
CreateFieldRequestSchema = marshmallow_dataclass.class_schema(
    CreateFieldRequest
)
