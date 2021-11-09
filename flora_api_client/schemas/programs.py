import marshmallow_dataclass
from flora_api_client.presentations.programs import (
    ProgramResponse, ProgramsResponse, Program
)


ProgramResponseSchema = marshmallow_dataclass.class_schema(
    ProgramResponse
)
ProgramsResponseSchema = marshmallow_dataclass.class_schema(
    ProgramsResponse
)
ProgramRequestSchema = marshmallow_dataclass.class_schema(
    Program
)
