from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional, List, Any

from .base import BaseDataclass, SuccessResponse, PagedResponse
from .enums import Currency, UnitOfWeight, UnitOfSize, UnitOfCount
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
    length: Decimal = field()
    height: Decimal = field()
    width: Decimal = field()
    size_unit: str = field(metadata={
        "validate": OneOf([r.value for r in UnitOfSize])
    })
    weight: Decimal = field()
    weight_unit: str = field(metadata={
        "validate": OneOf([r.value for r in UnitOfWeight])
    })


@dataclass(frozen=True)
class ProductItem(BaseDataclass):
    name: str = field(metadata={
        "validate": Length(max=150)
    })
    cnt: Decimal = field()
    unit: str = field(metadata={
        "validate": OneOf([r.value for r in UnitOfCount])
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
    items: Optional[List[ProductItem]] = field(default_factory=list)

    @property
    def main_image(self) -> Optional[Image]:
        if not self.images:
            return None
        for i in self.images:
            if i.position == 0:
                return i

    def __str__(self):
        return f'#{self.id} {self.name}'


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
    items: List[ProductItem] = field(default_factory=list, metadata={
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


@dataclass(frozen=True)
class FeaturedProductPrice(BaseDataclass):
    currency: str = field(metadata={
        "validate": Length(equal=3)
    })
    current: Decimal = field()
    old: Optional[Decimal] = field()
    discount: Decimal = field()
    discount_percent: int = field()


@dataclass(frozen=True)
class FeaturedProductExecutor(BaseDataclass):
    id: int = field(metadata={
        "strict": True,
    })
    name: str = field(metadata={
        'validate': Length(max=150)
    })
    url: str = field()
    price: FeaturedProductPrice = field()


@dataclass(frozen=True)
class FeaturedProduct(BaseDataclass):
    id: int = field(metadata={
        "strict": True,
    })
    name: str = field(metadata={
        'validate': Length(max=150, min=1)
    })
    description: Optional[str] = field(metadata={
        'validate': Length(max=1000)
    })
    data: Any = field()
    length: Decimal = field()
    width: Decimal = field()
    height: Decimal = field()
    size_unit: str = field(metadata={
        "validate": OneOf([r.value for r in UnitOfSize])
    })
    weight: Decimal = field()
    weight_unit: str = field(metadata={
        "validate": OneOf([r.value for r in UnitOfWeight])
    })
    images: List[Image] = field(default_factory=list, metadata={
        "required": True
    })
    executors: List[FeaturedProductExecutor] = field(
        default_factory=list, metadata={
            "required": True
        })
    items: List[ProductItem] = field(
        default_factory=list, metadata={
            "required": True
        }
    )


@dataclass(frozen=True)
class FeaturedProductsResponse(PagedResponse):
    result: List[FeaturedProduct] = field(default_factory=list, metadata={
        "required": True
    })


@dataclass(frozen=True)
class FeaturedProductsQuerystring(BaseDataclass):
    currency: str = field(metadata={
        "validate": OneOf([r.value for r in Currency])
    })
    page: Optional[int] = field(default=1)  # страница
    per_page: Optional[int] = field(
        default=10)  # количество элементов на странице

