from dataclasses import dataclass, field
from typing import Optional, List

from marshmallow.validate import Length

from .base import SuccessResponse, BaseDataclass, PagedResponse


@dataclass(frozen=True)
class TagBase(BaseDataclass):
    id: int = field(metadata={
        "strict": True,
    })
    name: str = field(metadata={
        'validate': Length(max=150, min=1)
    })


@dataclass(frozen=True)
class Tag(TagBase):
    parent_id: Optional[int] = field(metadata={
        "strict": True,
    })
    is_visible: bool = field(default=True)
    is_inherited: bool = field(default=False)


@dataclass(frozen=True)
class CreateTagRequest(BaseDataclass):
    name: str = field(metadata={
        'validate': Length(max=150, min=1)
    })
    parent_id: Optional[int] = field(metadata={
        "strict": True,
    })
    is_visible: Optional[bool] = field()


@dataclass(frozen=True)
class TagResponse(SuccessResponse):
    result: Tag = field()


@dataclass(frozen=True)
class TagsResponse(PagedResponse):
    result: List[Tag] = field(default_factory=list, metadata={
        "required": True
    })


@dataclass(frozen=True)
class TagsTreeItem(TagBase):
    children: Optional[List[TagBase]] = field()


@dataclass(frozen=True)
class TagsTreeResponse(SuccessResponse):
    result: List[TagsTreeItem] = field(default_factory=list, metadata={
        "required": True
    })

