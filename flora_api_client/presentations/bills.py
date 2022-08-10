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
    delivery_time: int = field()
    amount: Decimal = field()
    currency: str = field(metadata={
        "validate": Length(equal=3)
    })
    state: str = field()
    city_name: str = field()
    receiver_name: str = field(metadata={
        'validate': Length(max=150)
    })
    receiver_phone: str = field(metadata={
        "validate": Length(max=100)
    })
    delivery_address: str = field(metadata={
        "validate": Length(max=1000)
    })
    card_text: str = field(metadata={
        "validate": Length(max=1000)
    })


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
