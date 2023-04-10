from dataclasses import dataclass, field
from decimal import Decimal

from marshmallow import ValidationError
from marshmallow.validate import Length, OneOf, Range
from datetime import datetime

from .base import SuccessResponse, BaseDataclass, PagedResponse
from .enums import Currency
from .products import FeaturedProductExecutor


@dataclass
class PriceDataAction(BaseDataclass):
    percent: int = field(metadata={"strict": True, "validate": Range(min=-90, max=90)})
    start: datetime = field()
    end: datetime = field()

    def __post_init__(self):
        if self.start > self.end:
            raise ValidationError("Начало должно быть раньше окончания")


@dataclass
class PriceData(BaseDataclass):
    actions: list[PriceDataAction] = field(default_factory=list)

    def __post_init__(self):
        if len(self.actions) > 3:
            raise ValidationError(
                f"Максимальное количество действий 3. Сейчас: {len(self.actions)}"
            )


@dataclass
class PriceBase(BaseDataclass):
    product_id: int = field(
        metadata={
            "strict": True,
        }
    )
    price: Decimal = field()
    is_available: bool = field()
    data: PriceData = field()


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


@dataclass
class PriceResponse(SuccessResponse):
    result: Price = field()


@dataclass
class PricesResponse(PagedResponse):
    result: list[Price] = field(default_factory=list, metadata={"required": True})


@dataclass
class PricesRequest(BaseDataclass):
    currency: str = field(metadata={"validate": Length(equal=3)})
    prices: list[PriceBase] = field(default_factory=list, metadata={"required": True})


@dataclass
class CurrentPriceData(BaseDataclass):
    product_id: int = field(metadata={"strict": True})
    executors: list[FeaturedProductExecutor] = field(
        default_factory=list, metadata={"required": True}
    )


@dataclass
class PricesCurrentResponse(SuccessResponse):
    result: list[CurrentPriceData] = field(default=list, metadata={"required": True})


@dataclass
class PricesCurrentQuerystring(BaseDataclass):
    ids: str = field()
    city_id: int = field()
    promo: str | None = field()
    currency: str = field(
        metadata={"validate": OneOf([r.value for r in Currency])}, default="rub"
    )
