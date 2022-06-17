from dataclasses import dataclass, field
from typing import List, Optional, Any

from marshmallow.validate import Length

from .base import SuccessResponse, BaseDataclass
from .images import Image


@dataclass(frozen=True)
class SliderItemBase(BaseDataclass):
    id: int = field(metadata={
        "strict": True
    })
    description: str = field(metadata={
        "validate": Length(max=150)
    })
    desc_image_id: Optional[int] = field(metadata={
        "strict": True
    })
    mobile_image_id: Optional[int] = field(metadata={
        "strict": True
    })
    position: int = field(metadata={
        "strict": True
    })
    link: str = field(metadata={
        "validate": Length(max=250)
    })
    open_in_new_window: bool = field()
    enabled: bool = field()


@dataclass(frozen=True)
class SliderItem(SliderItemBase):
    desc_image: Optional[Image] = field()
    mobile_image: Optional[Image] = field()


@dataclass(frozen=True)
class Slider(BaseDataclass):
    items: List[SliderItem] = field(
        default_factory=list, metadata={
            "required": True
        })


@dataclass(frozen=True)
class SliderResponse(SuccessResponse):
    result: List[SliderItem] = field(
        default_factory=list, metadata={
            "required": True
        })


@dataclass(frozen=True)
class SliderItemRequest(SliderItemBase):
    pass


@dataclass(frozen=True)
class SliderItemResponse(SuccessResponse):
    result: SliderItem = field()
