import marshmallow_dataclass
from marshmallow import Schema, EXCLUDE
from flora_api_client.presentations.bookkeeping import (
    BookkeepingRow,
    EntriesResponse,
    SummaryResponse,
    SummaryRequest,
)

Schema.Meta.unknown = EXCLUDE


BookkeepingRowSchema = marshmallow_dataclass.class_schema(BookkeepingRow)
BookkeepingEntriesResponseSchema = marshmallow_dataclass.class_schema(EntriesResponse)
BookkeepingSummaryResponseSchema = marshmallow_dataclass.class_schema(SummaryResponse)
BookkeepingSummaryRequestSchema = marshmallow_dataclass.class_schema(SummaryRequest)
