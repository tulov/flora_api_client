from dataclasses import dataclass, field

from marshmallow.validate import Range, Length

from .base import (
    BaseDataclass
)


@dataclass(frozen=True)
class BindCityRequestDataclass(BaseDataclass):
    geoname_id: int = field(metadata={
        'strict': True
    })
    delivery_price: int = field(metadata={
        'validate': Range(min=0)
    })
    delivery_currency: str = field(metadata={
        'validate': Length(equal=3)
    })
