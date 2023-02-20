import marshmallow_dataclass
from flora_api_client.presentations.partners import (
    Partner,
    SetCitiesAvailableRequest,
    SetProductsAvailableRequest,
)
from marshmallow import Schema, EXCLUDE

Schema.Meta.unknown = EXCLUDE


PartnerSchema = marshmallow_dataclass.class_schema(Partner)
SetCitiesAvailableRequestSchema = marshmallow_dataclass.class_schema(
    SetCitiesAvailableRequest
)
SetProductsAvailableRequestSchema = marshmallow_dataclass.class_schema(
    SetProductsAvailableRequest
)
