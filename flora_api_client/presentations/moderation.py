from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, Any, Optional, List
from marshmallow.validate import Length, ContainsOnly

from .base import BaseDataclass, SuccessResponse, Pager
from .enums import ModerationAction, ModerationResult


@dataclass(frozen=True)
class RequestForModeration(BaseDataclass):
    id: int = field()
    action: str = field(metadata={
        'validate': ContainsOnly([a.value for a in ModerationAction]),
    })
    date_added: datetime = field()
    user_id: int = field()
    result: Optional[str] = field(metadata={
        'validate': ContainsOnly([r.value for r in ModerationResult]),
    })
    date_result: Optional[datetime] = field()
    admin_id: Optional[int] = field()
    cause: Optional[str] = field(metadata={
        'validate': Length(max=1500)
    })
    data: Dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class RequestsForModerationResponse(SuccessResponse):
    pager: Pager = field()
    result: List[RequestForModeration] = field(default_factory=list, metadata={
        "required": True
    })

