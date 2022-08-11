from dataclasses import dataclass, field
from decimal import Decimal
from typing import List

from marshmallow.validate import Length

from .base import (
    SuccessResponse, BaseDataclass, PagedResponse
)


@dataclass(frozen=True)
class PriceBase(BaseDataclass):
    product_id: int = field(metadata={
        "strict": True,
    })
    city_id: int = field(metadata={
        "strict": True,
    })
    price: Decimal = field()


@dataclass(frozen=True)
class Price(PriceBase):
    id: int = field(metadata={
        "strict": True,
    })
    currency: str = field(metadata={
        "validate": Length(equal=3)
    })
    partner_id: int = field(metadata={
        "strict": True,
    })
    current_usd_price: Decimal = field()
    discount_percent: int = field()


@dataclass(frozen=True)
class PriceResponse(SuccessResponse):
    result: Price = field()


@dataclass(frozen=True)
class PricesResponse(PagedResponse):
    result: List[Price] = field(default_factory=list, metadata={
        "required": True
    })


@dataclass(frozen=True)
class PricesRequest(BaseDataclass):
    currency: str = field(metadata={
        "validate": Length(equal=3)
    })
    prices: List[PriceBase] = field(default_factory=list, metadata={
        "required": True
    })
