from dataclasses import dataclass, field
from decimal import Decimal

from marshmallow.validate import Length, OneOf

from .base import SuccessResponse, BaseDataclass, PagedResponse
from .enums import Currency
from .products import FeaturedProductExecutor


@dataclass
class PriceBase(BaseDataclass):
    product_id: int = field(
        metadata={
            "strict": True,
        }
    )
    price: Decimal = field()
    discount_percent: int = field()
    is_available: bool = field()


@dataclass
class Price(PriceBase):
    id: int = field(
        metadata={
            "strict": True,
        }
    )
    currency: str = field(metadata={"validate": Length(equal=3)})
    partner_id: int = field(
        metadata={
            "strict": True,
        }
    )
    current_usd_price: Decimal = field()


@dataclass
class PriceResponse(SuccessResponse):
    result: Price = field()


@dataclass
class PricesResponse(PagedResponse):
    result: list[Price] = field(default_factory=list, metadata={"required": True})


@dataclass
class PricesRequest(BaseDataclass):
    currency: str = field(metadata={"validate": Length(equal=3)})
    delivery_price: Decimal = field()
    city_id: int = field(metadata={"strict": True})
    prices: list[PriceBase] = field(default_factory=list, metadata={"required": True})


@dataclass
class PriceData(BaseDataclass):
    product_id: int = field(metadata={"strict": True})
    executors: list[FeaturedProductExecutor] = field(
        default_factory=list, metadata={"required": True}
    )


@dataclass
class PricesCurrentResponse(SuccessResponse):
    result: list[PriceData] = field(default=list, metadata={"required": True})


@dataclass
class PricesCurrentQuerystring(BaseDataclass):
    ids: str = field()
    city_id: int = field()
    promo: str | None = field()
    currency: str = field(
        metadata={"validate": OneOf([r.value for r in Currency])}, default="rub"
    )
