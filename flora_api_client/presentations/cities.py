# from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional, List, Any
from decimal import Decimal

from marshmallow.validate import Length, OneOf

from .base import (
    SuccessResponse, BaseDataclass, PagedResponse
)


@dataclass(frozen=True)
class Continent(BaseDataclass):
    id: int = field(metadata={
        "strict": True
    })
    iso: str = field(metadata={
        'validate': Length(equal=2)
    })
    name: str = field(metadata={
        'validate': Length(max=30)
    })
    slug: str = field(metadata={
        'validate': Length(max=100)
    })


@dataclass(frozen=True)
class Subcontinent(BaseDataclass):
    id: int = field(metadata={
        "strict": True
    })
    continent_id: int = field(metadata={
        "strict": True
    })
    iso: str = field(metadata={
        'validate': Length(equal=3)
    })
    name: str = field(metadata={
        'validate': Length(max=30)
    })
    slug: str = field(metadata={
        'validate': Length(max=100)
    })
    continent: Optional[Continent] = field()


@dataclass(frozen=True)
class Country(BaseDataclass):
    id: int = field(metadata={
        "strict": True
    })
    subcontinent_id: int = field(metadata={
        "strict": True
    })
    iso: str = field(metadata={
        'validate': Length(equal=2)
    })
    populations: int = field(metadata={
        "strict": True,
    })
    name: str = field(metadata={
        'validate': Length(max=30)
    })
    slug: str = field(metadata={
        'validate': Length(max=100)
    })
    capital_id: Optional[int] = field(metadata={
        "strict": True
    })
    subcontinent: Optional[Subcontinent] = field()


@dataclass(frozen=True)
class Region(BaseDataclass):
    id: int = field(metadata={
        "strict": True
    })
    country_id: int = field(metadata={
        "strict": True
    })
    iso: str = field(metadata={
        'validate': Length(equal=4)
    })
    populations: Optional[int] = field(metadata={
        "strict": True,
    })
    name: str = field(metadata={
        'validate': Length(max=50)
    })
    slug: str = field(metadata={
        'validate': Length(max=100)
    })
    country: Optional[Country] = field()


@dataclass(frozen=True)
class City(BaseDataclass):
    id: int = field(metadata={
        "strict": True,
    })
    country_id: int = field(metadata={
        "strict": True
    })
    region_id: Optional[int] = field(metadata={
        "strict": True
    })
    parent_city_id: Optional[int] = field(metadata={
        "strict": True
    })
    lat: Decimal = field()
    lng: Decimal = field()
    name: str = field(metadata={
        "validate": Length(max=50)
    })
    slug: str = field(metadata={
        "validate": Length(max=100)
    })
    gmt: Optional[Decimal] = field()
    timezone: Optional[str] = field(metadata={
        "validate": Length(max=100)
    })
    country: Optional[Country] = field()
    parent_city: Optional[Any] = field()
    region: Optional[Region] = field()

    def __str__(self):
        s = self.name
        if self.parent_city:
            s += ", " + self.parent_city.name
        if self.region:
            s += ", " + self.region.name
        if self.country:
            s += ", " + self.country.name
        return s


@dataclass(frozen=True)
class CityResponse(SuccessResponse):
    result: City = field()


@dataclass(frozen=True)
class CitiesResponse(PagedResponse):
    result: List[City] = field(default_factory=list, metadata={
        "required": True
    })


@dataclass(frozen=True)
class SearchCity(BaseDataclass):
    id: int = field(metadata={
        "strict": True
    })
    name: str = field()


@dataclass(frozen=True)
class SearchCitiesResponse(SuccessResponse):
    result: List[SearchCity] = field(default_factory=list, metadata={
        "required": True
    })
