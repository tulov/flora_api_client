import datetime
from dataclasses import dataclass, field

from marshmallow.validate import Length

from .base import SuccessResponse, BaseDataclass, PagedResponse
from .validates import Phone


@dataclass
class Callback(BaseDataclass):
    phone: str = field(metadata={"validate": Phone()})
    id: int | None = field(
        metadata={
            "strict": True,
        },
        default=None,
    )
    comment: str | None = field(metadata={"validate": Length(max=1000)}, default=None)
    created_at: datetime | None = field(default=None)
    updated_at: datetime | None = field(default=None)


@dataclass
class CallbackResponse(SuccessResponse):
    result: Callback = field()


@dataclass
class CallbacksResponse(PagedResponse):
    result: list[Callback] = field(default_factory=list, metadata={"required": True})
