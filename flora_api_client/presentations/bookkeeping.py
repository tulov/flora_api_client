from dataclasses import dataclass, field
from datetime import datetime
from decimal import Decimal
from typing import Any

from marshmallow.validate import Length, OneOf

from .base import BaseDataclass
from .enums import PaymentTypes


@dataclass
class BookkeepingRow(BaseDataclass):
    id: int = field(metadata={"strict": True})
    created_at: datetime = field()
    user_id: int = field(metadata={"strict": True})
    amount: Decimal = field()
    currency: str = field(metadata={"validate": Length(equal=3)})
    type: str = field(metadata={"validate": OneOf([r.value for r in PaymentTypes])})
    order_id: int | None = field(metadata={"strict": True}, default=None)
    account_id: int | None = field(metadata={"strict": True}, default=None)
    data: dict[str, Any] = field(default_factory=dict)
