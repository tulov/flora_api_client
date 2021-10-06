from dataclasses import dataclass, field
from typing import Optional, List

from marshmallow.validate import Length

from .base import SuccessResponse, BaseDataclass, PagedResponse
from .tags import Tag
from .fields import Field


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
    is_visible: bool = field(default=True)
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
    tags: Optional[List[int]] = field(default_factory=list)


@dataclass(frozen=True)
class CategoryResponse(SuccessResponse):
    result: Category = field()


@dataclass(frozen=True)
class CategoriesResponse(PagedResponse):
    result: List[Category] = field(default_factory=list, metadata={
        "required": True
    })

