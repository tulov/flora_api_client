import marshmallow_dataclass
from flora_api_client.presentations.congratulations import (
    Congratulation,
    CongratulationResponse,
    OccasionResponse,
    Occasion,
    OccasionsResponse,
)
from marshmallow import Schema, EXCLUDE

Schema.Meta.unknown = EXCLUDE


CongratulationResponseSchema = marshmallow_dataclass.class_schema(
    CongratulationResponse
)
OccasionResponseSchema = marshmallow_dataclass.class_schema(OccasionResponse)
OccasionsResponseSchema = marshmallow_dataclass.class_schema(OccasionsResponse)
OccasionSchema = marshmallow_dataclass.class_schema(Occasion)
CongratulationSchema = marshmallow_dataclass.class_schema(Congratulation)
