from dataclasses import dataclass, field

from marshmallow.validate import Length

from .base import SuccessResponse, BaseDataclass


@dataclass(frozen=True)
class Category(BaseDataclass):
    id: int = field(metadata={
        "strict": True,
    })
    name: str = field(metadata={
        'validate': Length(max=150, min=1)
    })
    parent_id: int = field(metadata={
        "strict": True,
    })


@dataclass(frozen=True)
class CategoryResponse(SuccessResponse):
    result: Category = field()
