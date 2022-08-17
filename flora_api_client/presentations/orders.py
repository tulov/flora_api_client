from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional, List, Any
from datetime import date, datetime

from marshmallow.validate import Length, OneOf, Email

from .bills import Bill
from .users import User
from .cities import City
from .products import Product

from .base import (
    SuccessResponse, BaseDataclass, PagedResponse
)
from .validates import Phone
from .enums import OrderState


@dataclass(frozen=True)
class OrderProduct(BaseDataclass):
    product_id: int = field(metadata={
        "strict": True
    })
    cnt: int = field(metadata={
        "strict": True
    })


@dataclass(frozen=True)
class OrderItem(OrderProduct):
    order_id: int = field(metadata={
        "strict": True
    })
    product_id: int = field(metadata={
        "strict": True
    })
    cnt: int = field(metadata={
        "strict": True
    })
    price: Decimal = field()
    currency: str = field(metadata={
        "validate": Length(equal=3)
    })
    provider_id: int = field(metadata={
        "strict": True
    })
    data: Any = field()
    product: Optional[Product] = field()
    provider: Optional[User] = field()


@dataclass(frozen=True)
class Order(BaseDataclass):
    id: int = field(metadata={
        "strict": True
    })
    guid: str = field()
    parent_id: Optional[int] = field(metadata={
        "strict": True
    })
    city_id: int = field(metadata={
        "strict": True
    })
    order_datetime: datetime = field()
    delivery_date: date = field()
    delivery_time: int = field(metadata={
        "strict": True
    })
    receiver_name: str = field(metadata={
        "validate": Length(max=150)
    })
    receiver_phone: str = field(metadata={
        "validate": Length(max=100)
    })
    delivery_address: str = field(metadata={
        "validate": Length(max=1000)
    })
    card_text: str = field(metadata={
        "validate": Length(max=1000)
    })
    take_photo_with_receiver: bool = field()
    send_sms_about_delivery: bool = field()
    user_id: int = field(metadata={
        "strict": True
    })
    provider_id: int = field(metadata={
        "strict": True
    })
    state: str = field(metadata={
        "validate": OneOf([r.value for r in OrderState])
    })
    promo_code: str = field(metadata={
        "validate": Length(max=100)
    })
    amount: Decimal = field()
    currency: str = field(metadata={
        "validate": Length(equal=3)
    })
    city: Optional[City] = field()
    provider: Optional[User] = field()
    user: Optional[User] = field()
    bill: Optional[Bill] = field()
    is_complicated: Optional[bool] = field(default=False)
    items: Optional[List[OrderItem]] = field(default_factory=list)
    children: Optional[List[Any]] = field(default_factory=list)


@dataclass(frozen=True)
class CreateOrderRequest(BaseDataclass):
    guid: str = field()
    delivery_date: date = field()
    city_id: int = field(metadata={
        "strict": True
    })
    delivery_time: int = field(metadata={
        "strict": True
    })
    sender_email: Optional[str] = field(metadata={
        "validate": Email()
    })
    sender_phone: Optional[str] = field(metadata={
        "validate": Phone()
    })
    receiver_name: str = field(metadata={
        'validate': Length(max=150)
    })
    receiver_phone: str = field(metadata={
        "validate": Length(max=100)
    })
    delivery_address: str = field(metadata={
        "validate": Length(max=1000)
    })
    card_text: str = field(metadata={
        "validate": Length(max=1000)
    })
    promo_code: Optional[str] = field()
    user_sum: Decimal = field()
    currency: str = field(metadata={
        "validate": Length(equal=3)
    })
    take_photo_with_receiver: bool = field(default=False),
    send_sms_about_delivery: bool = field(default=False),
    products: List[OrderProduct] = field(
        default_factory=list, metadata={
            "required": True
        })


@dataclass(frozen=True)
class OrderResponse(SuccessResponse):
    result: Order = field()


@dataclass(frozen=True)
class OrdersResponse(PagedResponse):
    result: List[Order] = field(default_factory=list, metadata={
        "required": True
    })
