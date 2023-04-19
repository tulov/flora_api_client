from dataclasses import dataclass, field
from datetime import datetime
from typing import Any

from marshmallow import ValidationError
from marshmallow.fields import Decimal
from marshmallow.validate import ContainsOnly, Length, Range, Email, OneOf, Regexp

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
class WorkScheduleItem(BaseDataclass):
    start: str = field(
        metadata={"validate": Regexp("(^([0-1][0-9]|2[0-3]):[0-5][0-9]$)|^$")}
    )
    end: str = field(
        metadata={"validate": Regexp("(^([0-1][0-9]|2[0-3]):[0-5][0-9]$)|^$")}
    )

    def __post_init__(self):
        if not self.start and self.end:
            raise ValidationError({"_schema": ["Не указано начало диапазона"]})
        if self.start and not self.end:
            raise ValidationError({"_schema": ["Не указан конец диапазона"]})
        if self.start and self.end:
            start = datetime.strptime(self.start, "%H:%M").time()
            end = datetime.strptime(self.end, "%H:%M").time()
            if start >= end:
                raise ValidationError(
                    {"_schema": ["Начало диапазона должно быть больше его завершения"]}
                )


@dataclass
class WorkSchedule(BaseDataclass):
    monday: WorkScheduleItem | None = field(default=None)
    tuesday: WorkScheduleItem | None = field(default=None)
    wednesday: WorkScheduleItem | None = field(default=None)
    thursday: WorkScheduleItem | None = field(default=None)
    friday: WorkScheduleItem | None = field(default=None)
    saturday: WorkScheduleItem | None = field(default=None)
    sunday: WorkScheduleItem | None = field(default=None)


@dataclass
class UserData(BaseDataclass):
    address: str | None = field(metadata={"validate": Length(max=200)}, default=None)
    promo_system: str | None = field(
        metadata={"validate": OneOf([r.value for r in PromoSystems])},
        default=PromoSystems.cashback.value,
    )
    work_schedule: WorkSchedule | None = field(default=None)
    old_id: int | None = field(default=None)
    cashback: Decimal = field(default=Decimal(0))


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
    data: UserData = field(default_factory=UserData)
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
        if self.data and hasattr(self.data, "promo_system"):
            return self.data.promo_system
        return PromoSystems.cashback.value

    @property
    def cashback(self) -> Decimal:
        if self.data and hasattr(self.data, "cashback"):
            return self.data.cashback
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
