from dataclasses import dataclass, field
from typing import Optional, List

from marshmallow.validate import Length, OneOf

from .base import (
    SuccessResponse, BaseDataclass, PagedResponse
)


@dataclass(frozen=True)
class City(BaseDataclass):
    id: int = field(metadata={
        "strict": True,
    })
    locale_code: str = field(metadata={
        'validate': Length(max=5, min=2)
    })
    continent_code: str = field(metadata={
        "validate": Length(equal=2)
    })
    continent_name: str = field(metadata={
        "validate": Length(max=30)
    })
    country_iso_code: Optional[str] = field(metadata={
        "validate": Length(max=2)
    })
    country_name: Optional[str] = field(metadata={
        "validate": Length(max=50)
    })
    subdivision_1_iso_code: Optional[str] = field(metadata={
        "validate": Length(max=3)
    })
    subdivision_1_name: Optional[str] = field()
    subdivision_2_iso_code: Optional[str] = field(metadata={
        "validate": Length(max=3)
    })
    subdivision_2_name: Optional[str] = field()
    city_name: Optional[str] = field()
    metro_code: Optional[int] = field()
    time_zone: Optional[str] = field()
    is_in_european_union: bool = field()
    postal_code: Optional[str] = field()
    latitude: Optional[float] = field()
    longitude: Optional[float] = field()
    delivery_price: Optional[int] = field()
    delivery_currency: Optional[str] = field()

    def __str__(self):
        s1 = f', {self.subdivision_1_name}' if self.subdivision_1_name else ''
        s2 = f', {self.subdivision_2_name}' if self.subdivision_2_name else ''
        c = f', {self.city_name}' if self.city_name else ''
        return f'{self.country_name}{s1},{s2}{c}'


@dataclass(frozen=True)
class CityResponse(SuccessResponse):
    result: City = field()


@dataclass(frozen=True)
class CitiesResponse(PagedResponse):
    result: List[City] = field(default_factory=list, metadata={
        "required": True
    })
