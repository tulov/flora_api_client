from dataclasses import dataclass, field
from typing import Optional, List

from marshmallow.validate import Length, OneOf

from .base import SuccessResponse, BaseDataclass, PagedResponse
from .enums import Currency
from .tags import Tag
from .fields import Field, Relationship


@dataclass(frozen=True)
class Category(BaseDataclass):
    id: int = field(metadata={
        "strict": True,
    })
    name: str = field(metadata={
        'validate': Length(max=150, min=1)
    })
    parent_id: Optional[int] = field(metadata={
        "strict": True,
    })
    slug: str = field(metadata={
        "validate": Length(max=100, min=1)
    })
    is_visible: bool = field(default=True)
    weight: int = field(default=0)
    tags: Optional[List[Tag]] = field(default_factory=list)
    fields: Optional[List[Field]] = field(default_factory=list)


@dataclass(frozen=True)
class CreateCategoryRequest(BaseDataclass):
    name: str = field(metadata={
        'validate': Length(max=150, min=1)
    })
    parent_id: Optional[int] = field(metadata={
        "strict": True,
    })
    is_visible: Optional[bool] = field()
    slug: str = field(metadata={
        "validate": Length(max=100, min=1)
    })
    weight: int = field(default=0)
    tags: Optional[List[int]] = field(default_factory=list)
    fields: Optional[List[Relationship]] = field(default_factory=list)


@dataclass(frozen=True)
class CategoryResponse(SuccessResponse):
    result: Category = field()


@dataclass(frozen=True)
class CategoriesResponse(PagedResponse):
    result: List[Category] = field(default_factory=list, metadata={
        "required": True
    })


@dataclass(frozen=True)
class TagCounter(BaseDataclass):
    tag_id: int = field(metadata={
        "strict": True
    })
    count: int = field(metadata={
        "strict": True
    })


@dataclass(frozen=True)
class FilterCounterResult(BaseDataclass):
    count: int = field(metadata={
        "strict": True
    })
    tags: List[TagCounter] = field(default_factory=list, metadata={
        "required": True
    })


@dataclass(frozen=True)
class FilterCounterResponse(SuccessResponse):
    result: FilterCounterResult = field()


@dataclass(frozen=True)
class FilterCounterRequest(BaseDataclass):
    city_id: int = field(metadata={
        "strict": True
    })
    category_id: int = field(metadata={
        "strict": True
    })
    price_from: Optional[int] = field(metadata={
        "strict": True
    })
    price_to: Optional[int] = field(metadata={
        "strict": True
    })
    currency: str = field(metadata={
        "validate": OneOf([r.value for r in Currency])
    }, default="rub")
    selected: List[int] = field(default_factory=list, metadata={
        "required": True
    })
    ids: List[int] = field(default_factory=list, metadata={
        "required": True
    })
