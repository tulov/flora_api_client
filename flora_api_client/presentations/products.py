from dataclasses import dataclass, field
from typing import Optional, List

from .base import BaseDataclass, SuccessResponse, PagedResponse
from .images import Image
from marshmallow.validate import Length


@dataclass(frozen=True)
class ProductBaseDataclass(BaseDataclass):
    category_id: int = field(metadata={
        "strict": True,
    })
    name: str = field(metadata={
        'validate': Length(max=150, min=1)
    })
    description: Optional[str] = field(metadata={
        'validate': Length(max=1000, min=1)
    })
    data: Optional[str] = field()


@dataclass(frozen=True)
class Product(ProductBaseDataclass):
    id: int = field(metadata={
        "strict": True,
    })
    owner_id: int = field(metadata={
        "strict": True,
    })
    is_moderated: Optional[bool] = field()
    is_template: bool = field(default=False)


@dataclass(frozen=True)
class ProductRequest(ProductBaseDataclass):
    tags: List[int] = field(default_factory=list, metadata={
        "required": True
    })
    files: List[Image] = field(default_factory=list, metadata={
        "required": True
    })


@dataclass(frozen=True)
class ProductResponse(SuccessResponse):
    result: Product = field()


@dataclass(frozen=True)
class ProductsResponse(PagedResponse):
    result: List[Product] = field(default_factory=list, metadata={
        "required": True
    })
