from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional, List, Dict, Any

from marshmallow.validate import Length, OneOf

from .base import SuccessResponse, BaseDataclass, PagedResponse
from .enums import PromoTypes


@dataclass(frozen=True)
class PromoCode(BaseDataclass):
    code: str = field(metadata={
        "validate": Length(max=30)
    })
    type: str = field(metadata={
        'validate': OneOf([r.value for r in PromoTypes])
    })
    is_valid: bool = field()
    data: Dict[str, Any] = field(default_factory=dict)
    created_at: Optional[datetime] = field(default=None)


@dataclass(frozen=True)
class PromoCodeResponse(SuccessResponse):
    result: PromoCode = field()


@dataclass(frozen=True)
class PromoCodesResponse(PagedResponse):
    result: List[PromoCode] = field(default_factory=list, metadata={
        "required": True
    })
