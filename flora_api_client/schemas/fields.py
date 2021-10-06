import marshmallow_dataclass
from flora_api_client.presentations.fields import (
    FieldResponse, CreateFieldRequest, FieldsResponse, Relationship
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
RelationshipSchema = marshmallow_dataclass.class_schema(
    Relationship
)
