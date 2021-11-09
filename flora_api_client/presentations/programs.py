from decimal import Decimal
from datetime import datetime
from dataclasses import dataclass, field
from typing import Optional, List

from marshmallow import ValidationError
from marshmallow.validate import Length, OneOf

from .base import (
    SuccessResponse, BaseDataclass, PagedResponse
)
from .enums import ProgramAction, ProgramType
from .products import Product
from .cities import City


@dataclass(frozen=True)
class Program(BaseDataclass):
    id: Optional[int] = field(metadata={
        "strict": True,
    })
    partner_id: int = field(metadata={
        "strict": True,
    })
    title: str = field(metadata={
        "validate": Length(max=100)
    })
    description: Optional[str] = field()
    type: str = field(metadata={
        'validate': OneOf([r.value for r in ProgramType]),
    })
    action: str = field(metadata={
        'validate': OneOf([r.value for r in ProgramAction]),
    })
    value: Decimal = field()
    currency: Optional[str] = field(metadata={
        "validate": Length(equal=3)
    })
    start: Optional[datetime] = field()
    end: Optional[datetime] = field()
    product_ids: List[int] = field(default_factory=list)
    geoname_ids: List[int] = field(default_factory=list)
    products: Optional[List[Product]] = field(default_factory=list)
    cities: Optional[List[City]] = field(default_factory=list)

    def __post_init__(self):
        if self.start and self.end and self.start > self.end:
            raise ValidationError("'Start' should be less then 'end'")


@dataclass(frozen=True)
class ProgramResponse(SuccessResponse):
    result: Program = field()


@dataclass(frozen=True)
class ProgramsResponse(PagedResponse):
    result: List[Program] = field(default_factory=list, metadata={
        "required": True
    })
