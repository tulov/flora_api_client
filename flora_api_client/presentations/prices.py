from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional, List

from marshmallow.validate import Length, OneOf

from .base import (
    SuccessResponse, BaseDataclass, PagedResponse
)
from .products import Product
from .cities import City


@dataclass(frozen=True)
class Price(BaseDataclass):
    id: int = field(metadata={
        "strict": True,
    })
    product_id: int = field(metadata={
        "strict": True,
    })
    geoname_id: int = field(metadata={
        "strict": True,
    })
    price: Decimal = field()
    currency: str = field(metadata={
        "validate": Length(equal=3)
    })
    product: Optional[Product] = field()
    city: Optional[City] = field()


@dataclass(frozen=True)
class PriceResponse(SuccessResponse):
    result: Price = field()


@dataclass(frozen=True)
class PricesResponse(PagedResponse):
    result: List[Price] = field(default_factory=list, metadata={
        "required": True
    })
