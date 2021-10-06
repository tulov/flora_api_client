from dataclasses import dataclass, field
from typing import Optional, List

from marshmallow.validate import Length, OneOf

from .base import (
    SuccessResponse, BaseDataclass, PagedResponse
)
from .enums import FieldType


@dataclass(frozen=True)
class FieldBaseDataclass(BaseDataclass):
    name: str = field(metadata={
        'validate': Length(max=150, min=1)
    })
    help: Optional[str] = field(metadata={
        'validate': Length(max=200)
    })
    type: str = field(metadata={
        'validate': OneOf([r.value for r in FieldType]),
    })


@dataclass(frozen=True)
class Field(FieldBaseDataclass):
    id: int = field(metadata={
        "strict": True,
    })


@dataclass(frozen=True)
class CreateFieldRequest(FieldBaseDataclass):
    pass


@dataclass(frozen=True)
class FieldResponse(SuccessResponse):
    result: Field = field()


@dataclass(frozen=True)
class FieldsResponse(PagedResponse):
    result: List[Field] = field(default_factory=list, metadata={
        "required": True
    })
