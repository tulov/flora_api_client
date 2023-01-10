import marshmallow_dataclass
from marshmallow import Schema, EXCLUDE
from flora_api_client.presentations.bookkeeping import BookkeepingRow

Schema.Meta.unknown = EXCLUDE


BookkeepingRowSchema = marshmallow_dataclass.class_schema(BookkeepingRow)
