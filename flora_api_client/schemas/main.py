import marshmallow_dataclass
from flora_api_client.presentations.main import ApplicationInfoResponse


ApplicationInfoResponseSchema = marshmallow_dataclass.class_schema(
    ApplicationInfoResponse
)
