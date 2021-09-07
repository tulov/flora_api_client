import marshmallow_dataclass
from flora_api_client.presentations.counters import CountersResponse


CountersResponseSchema = marshmallow_dataclass.class_schema(
    CountersResponse
)
