from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional, List, Any
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
    revision: int = field(metadata={
        "strict": True,
    })
    data: Any = field(default_factory=dict)
    result: Optional[str] = field(metadata={
        'validate': OneOf([r.value for r in ModerationResult]),
    }, default=None)
    date_result: Optional[datetime] = field(default=None)
    admin_id: Optional[int] = field(default=None)
    cause: Optional[str] = field(metadata={
        'validate': Length(max=1500)
    }, default=None)
    user: Optional[User] = field(default=None)
    admin: Optional[User] = field(default=None)
    obj_id: Optional[int] = field(default=None)


@dataclass(frozen=True)
class RequestsForModerationResponse(PagedResponse):
    result: List[RequestForModeration] = field(default_factory=list, metadata={
        "required": True
    })


@dataclass(frozen=True)
class RequestForModerationResponse(SuccessResponse):
    result: RequestForModeration = field()


@dataclass(frozen=True)
class ModerationUpdateRequest(BaseDataclass):
    result: str = field(metadata={
        'validate': OneOf([r.value for r in ModerationResult]),
    })
    cause: Optional[str] = field(metadata={
        'validate': Length(max=1500)
    })
    revision: int = field(metadata={
        "strict": True,
    })
