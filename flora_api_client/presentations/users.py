from dataclasses import dataclass, field
from datetime import datetime
from typing import Any

from marshmallow import ValidationError
from marshmallow.fields import Decimal
from marshmallow.validate import ContainsOnly, Length, Range, Email

from .base import BaseDataclass, SuccessResponse, Pager
from .enums import Roles, PromoSystems
from .validates import UniqueItems, Filled, Phone


@dataclass
class DataForAuth(BaseDataclass):
    id: int = field(
        metadata={
            "strict": True,
        }
    )
    service: str = field(metadata={"validate": Length(max=20, min=1)})
    is_checked: bool = field()
    value: str = field()
    data: dict[str, Any] = field(default_factory=dict)
    _confirm_data: str | None = field(default=None)
    _confirm_attempt_counter: int | None = field(default=None)
    _last_request_code: datetime | None = field(default=None)

    def get_confirm_data(self) -> str | None:
        return self._confirm_data

    def get_confirm_attempt_counter(self) -> int | None:
        return self._confirm_attempt_counter

    def get_last_request_code(self) -> datetime | None:
        return self._last_request_code


@dataclass
class Contacts(BaseDataclass):
    phone: str | None = field(metadata={"validate": Phone()})
    email: str | None = field(metadata={"validate": Email()})
    whatsapp: str | None = field(metadata={"validate": Phone()})


@dataclass
class User(BaseDataclass):
    id: int = field(
        metadata={
            "strict": True,
        }
    )
    registration_date: datetime = field()
    name: str = field(metadata={"validate": Length(max=150)})
    discount: int = field(metadata={"strict": True, "validate": Range(min=0, max=100)})
    send_sms: bool = field()
    send_email: bool = field()
    language: str = field(metadata={"validate": Length(equal=2)})
    currency: str = field(metadata={"validate": Length(equal=3)})
    is_moderated: bool = field()
    banned: bool = field()
    percent_us: int = field(
        metadata={
            "strict": True,
            "validate": Range(min=0, max=100),
        }
    )
    contacts: Contacts | None = field(default=None)
    data: dict[str, Any] = field(default_factory=dict)
    data_for_auth: list[DataForAuth] | None = field(default_factory=list)
    roles: list[str] = field(
        default_factory=list,
        metadata={
            "validate": [
                ContainsOnly([role.value for role in Roles]),
                UniqueItems(),
                Filled(),
            ],
            "required": True,
        },
    )
    _salt: str | None = field(default=None)
    _password: str | None = field(default=None)

    def get_salt(self) -> str | None:
        return self._salt

    def get_password(self) -> str | None:
        return self._password

    @property
    def promo_system(self) -> str:
        if self.data and "promo_system" in self.data:
            return self.data["promo_system"]
        return PromoSystems.cashback.value

    @property
    def cashback(self) -> Decimal:
        if self.data and "cashback" in self.data:
            return self.data["cashback"]
        return Decimal(0)


@dataclass
class RegistrationUserData(BaseDataclass):
    password: str = field(metadata={"validate": Length(min=6, max=30)})
    phone: str | None = field(metadata={"validate": Phone()})
    email: str | None = field(metadata={"validate": Email()})
    name: str | None = field(metadata={"validate": Length(min=1, max=150)})
    language: str = field(metadata={"validate": Length(equal=2)})
    currency: str = field(metadata={"validate": Length(equal=3)})
    address: str = field(metadata={"validate": Length(max=200)})
    send_sms: bool = field(default=True)
    send_email: bool = field(default=True)

    def __post_init__(self):
        if not self.phone and not self.email:
            raise ValidationError(
                {
                    "_schema": [
                        "You need to fill in at least "
                        'one field from "email" or "phone"'
                    ]
                }
            )


@dataclass
class ConfirmDataForAuthRequest(BaseDataclass):
    code: str = field(metadata={"validate": Length(min=4, max=20)})


@dataclass
class UsersResponse(SuccessResponse):
    pager: Pager = field()
    result: list[User] = field(default_factory=list, metadata={"required": True})


@dataclass
class ChangePasswordRequest(BaseDataclass):
    old_password: str = field(metadata={"validate": Length(min=6, max=30)})
    new_password: str = field(metadata={"validate": Length(min=6, max=30)})

    def __post_init__(self):
        if self.old_password == self.new_password:
            raise ValidationError(
                {"_schema": ["New password should be different with old password"]}
            )
