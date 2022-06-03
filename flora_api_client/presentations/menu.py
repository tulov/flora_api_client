from dataclasses import dataclass, field
from typing import List, Optional, Any

from marshmallow.validate import Length

from .base import SuccessResponse, BaseDataclass
from .images import Image


@dataclass(frozen=True)
class MenuItemBase(BaseDataclass):
    id: int = field(metadata={
        "strict": True
    })
    name: str = field(metadata={
        "validate": Length(max=100, min=1)
    })
    parent_id: Optional[int] = field(metadata={
        "strict": True
    })
    position: int = field(metadata={
        "strict": True
    })
    link: str = field(metadata={
        "validate": Length(max=250)
    })


@dataclass(frozen=True)
class MenuItem(MenuItemBase):
    image: Optional[Image] = field()
    children: Optional[List[Any]] = field()


@dataclass(frozen=True)
class Menu(BaseDataclass):
    items: List[MenuItem] = field(
        default_factory=list, metadata={
            "required": True
        })


@dataclass(frozen=True)
class MenuResponse(SuccessResponse):
    result: Menu = field()


@dataclass(frozen=True)
class MenuItemRequest(MenuItemBase):
    pass


@dataclass(frozen=True)
class MenuItemResponse(SuccessResponse):
    result: MenuItem = field()
