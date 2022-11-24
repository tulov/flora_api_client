from dataclasses import dataclass, field
from typing import Optional, List

from marshmallow.validate import Range, Length

from .base import (
    BaseDataclass, SuccessResponse
)
from .users import User


@dataclass(frozen=True)
class PartnerBindCityData(BaseDataclass):
    city_id: int = field(metadata={
        'strict': True
    })
    delivery_price: int = field(metadata={
        'validate': Range(min=0)
    })


@dataclass(frozen=True)
class Partner(User):
    cities: Optional[List[PartnerBindCityData]] = field(default=None)


@dataclass(frozen=True)
class BindCityRequestDataclass(BaseDataclass):
    city_id: int = field(metadata={
        'strict': True
    })
    delivery_price: int = field(metadata={
        'validate': Range(min=0)
    })
    delivery_currency: str = field(metadata={
        'validate': Length(equal=3)
    })


@dataclass(frozen=True)
class PartnerSettings(BaseDataclass):
    address: str = field(metadata={"validate": Length(max=200)})


@dataclass(frozen=True)
class PartnerSettingsRequest(BaseDataclass):
    settings: PartnerSettings = field()
    revision: int = field(metadata={"strict": True})


@dataclass(frozen=True)
class PartnerSettingsR(BaseDataclass):
    on_moderation: Optional[PartnerSettings] = field()
    on_site: PartnerSettings = field()
    revision: int = field(metadata={"strict": True})


@dataclass(frozen=True)
class PartnerSettingsResponse(SuccessResponse):
    result: PartnerSettingsR = field()
