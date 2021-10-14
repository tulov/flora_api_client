from dataclasses import dataclass, field
from typing import Optional, List

from .base import BaseDataclass, SuccessResponse, PagedResponse
from .images import Image
from .tags import Tag
from .categories import Category
from .moderation import RequestForModeration
from marshmallow.validate import Length, OneOf


@dataclass(frozen=True)
class ProductBaseDataclass(BaseDataclass):
    category_id: int = field(metadata={
        "strict": True,
    })
    name: str = field(metadata={
        'validate': Length(max=150, min=1)
    })
    description: Optional[str] = field(metadata={
        'validate': Length(max=1000)
    })
    data: Optional[str] = field()
    revision: int = field(metadata={
        "strict": True,
    })


@dataclass(frozen=True)
class Product(ProductBaseDataclass):
    id: int = field(metadata={
        "strict": True,
    })
    owner_id: int = field(metadata={
        "strict": True,
    })
    category: Optional[Category] = field()
    request_for_moderation: Optional[RequestForModeration] = field()
    is_template: bool = field(default=False)
    tags: Optional[List[Tag]] = field(default_factory=list)
    images: Optional[List[Image]] = field(default_factory=list)

    @property
    def main_image(self) -> Optional[Image]:
        if not self.images:
            return None
        for i in self.images:
            if i.position == 0:
                return i


@dataclass(frozen=True)
class FilesData(BaseDataclass):
    id: int = field(metadata={
        "strict": True,
    })
    position: int = field(metadata={
        "strict": True,
    })


@dataclass(frozen=True)
class ProductRequest(ProductBaseDataclass):
    tags: List[int] = field(default_factory=list, metadata={
        "required": True
    })
    files: List[FilesData] = field(default_factory=list, metadata={
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
