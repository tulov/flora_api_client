from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Any, Dict, Optional
from datetime import datetime, date

from marshmallow.validate import Length

from .base import (
    SuccessResponse, BaseDataclass, PagedResponse
)


@dataclass(frozen=True)
class BillOrderData(BaseDataclass):
    id: int = field(metadata={
        "strict": True
    })
    city_id: int = field(metadata={
        "strict": True
    })
    delivery_date: date = field()
    amount: Decimal = field()
    currency: str = field(metadata={
        "validate": Length(equal=3)
    })
    state: str = field()
    city_name: str = field()


@dataclass(frozen=True)
class Bill(BaseDataclass):
    guid: str = field()
    created_at: datetime = field()
    user_id: int = field(metadata={
        "strict": True
    })
    order_id: int = field(metadata={
        "strict": True
    })
    amount: Decimal = field()
    currency: str = field(metadata={
        "validate": Length(equal=3)
    })
    is_payed: bool = field()
    order_data: Optional[BillOrderData] = field()
    data: Dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class BillResponse(SuccessResponse):
    result: Bill = field()


@dataclass(frozen=True)
class BillsResponse(PagedResponse):
    result: List[Bill] = field(default_factory=list, metadata={
        "required": True
    })
