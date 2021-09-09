from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional, List
from marshmallow.validate import Length, OneOf

from .base import BaseDataclass, SuccessResponse, Pager
from .enums import ModerationAction, ModerationResult


@dataclass(frozen=True)
class RequestForModeration(BaseDataclass):
    id: int = field()
    action: str = field(metadata={
        'validate': OneOf([a.value for a in ModerationAction]),
    })
    date_added: datetime = field()
    user_id: int = field()
    result: Optional[str] = field(metadata={
        'validate': OneOf([r.value for r in ModerationResult]),
    })
    date_result: Optional[datetime] = field()
    admin_id: Optional[int] = field()
    cause: Optional[str] = field(metadata={
        'validate': Length(max=1500)
    })
    data: str = field()


@dataclass(frozen=True)
class RequestsForModerationResponse(SuccessResponse):
    pager: Pager = field()
    result: List[RequestForModeration] = field(default_factory=list, metadata={
        "required": True
    })

