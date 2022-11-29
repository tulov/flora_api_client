from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional

from marshmallow.validate import Length, OneOf

from .base import (
    SuccessResponse, BaseDataclass, PagedResponse
)
from .enums import Currency
from .products import FeaturedProductExecutor


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
    delivery_price: Optional[Decimal] = field(default=None)


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


@dataclass(frozen=True)
class PriceData(BaseDataclass):
    product_id: int = field(metadata={
        "strict": True
    })
    executors: List[FeaturedProductExecutor] = field(
        default_factory=list, metadata={
            "required": True
        })


@dataclass(frozen=True)
class PricesCurrentResponse(SuccessResponse):
    result: List[PriceData] = field(default=list, metadata={
        "required": True
    })


@dataclass(frozen=True)
class PricesCurrentQuerystring(BaseDataclass):
    ids: str = field()
    city_id: int = field()
    currency: str = field(metadata={
        "validate": OneOf([r.value for r in Currency])
    }, default="rub")
