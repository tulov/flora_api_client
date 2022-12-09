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

    def check(self) -> bool:
        if not self.is_valid:
            return False
        if 'period' in self.data:
            cur_date = datetime.now().date()
            arr = self.data['period'].split(" - ")
            start = datetime.strptime(arr[0], "%d.%m.%Y")
            end = datetime.strptime(arr[1], "%d.%m.%Y")
            return start <= cur_date <= end
        return True


@dataclass(frozen=True)
class PromoCodeResponse(SuccessResponse):
    result: PromoCode = field()


@dataclass(frozen=True)
class PromoCodesResponse(PagedResponse):
    result: List[PromoCode] = field(default_factory=list, metadata={
        "required": True
    })
