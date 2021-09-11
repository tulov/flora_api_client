from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional, List
from marshmallow.validate import Length, OneOf

from .base import BaseDataclass, PagedResponse, SuccessResponse
from .enums import ModerationAction, ModerationResult
from .users import User


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
    user: Optional[User] = field()


@dataclass(frozen=True)
class RequestsForModerationResponse(PagedResponse):
    result: List[RequestForModeration] = field(default_factory=list, metadata={
        "required": True
    })


@dataclass(frozen=True)
class RequestForModerationResponse(SuccessResponse):
    result: RequestForModeration = field()


@dataclass(frozen=True)
class ModerateRequest(BaseDataclass):
    result: str = field(metadata={
        'validate': OneOf([r.value for r in ModerationResult]),
    })
    cause: Optional[str] = field(metadata={
        'validate': Length(max=1500)
    })
