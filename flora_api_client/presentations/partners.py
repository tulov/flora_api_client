from dataclasses import dataclass, field

from marshmallow.validate import Range, Length

from .base import BaseDataclass, SuccessResponse
from .prices import Price
from .users import User


@dataclass
class PartnerBindCityData(BaseDataclass):
    city_id: int = field(metadata={"strict": True})
    delivery_price: int = field(metadata={"validate": Range(min=0)})


@dataclass
class Partner(User):
    cities: list[PartnerBindCityData] | None = field(default_factory=list)
    prices: list[Price] | None = field(default_factory=list)


@dataclass
class BindCityRequestDataclass(BaseDataclass):
    city_id: int = field(metadata={"strict": True})
    delivery_price: int = field(metadata={"validate": Range(min=0)})
    delivery_currency: str = field(metadata={"validate": Length(equal=3)})


@dataclass
class PartnerSettings(BaseDataclass):
    address: str = field(metadata={"validate": Length(max=200)})


@dataclass
class PartnerSettingsRequest(BaseDataclass):
    settings: PartnerSettings = field()
    revision: int = field(metadata={"strict": True})


@dataclass
class PartnerSettingsR(BaseDataclass):
    on_moderation: PartnerSettings | None = field()
    on_site: PartnerSettings = field()
    revision: int = field(metadata={"strict": True})


@dataclass
class PartnerSettingsResponse(SuccessResponse):
    result: PartnerSettingsR = field()


@dataclass
class SetProductsAvailableRequest(BaseDataclass):
    products_ids: list[int] = field()
    available: bool = field()


@dataclass
class SetCitiesAvailableRequest(BaseDataclass):
    cities_ids: list[int] = field()
    available: bool = field()
