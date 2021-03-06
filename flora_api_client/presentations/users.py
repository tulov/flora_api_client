from typing import List, Dict, Any, Optional
from dataclasses import dataclass, field

from marshmallow import ValidationError
from marshmallow.validate import ContainsOnly, Length, Range, Email
from datetime import datetime
from .enums import Roles
from .validates import UniqueItems, Filled, Phone
from .base import BaseDataclass, SuccessResponse, Pager


@dataclass(frozen=True)
class DataForAuth(BaseDataclass):
    id: int = field(metadata={
        "strict": True,
    })
    service: str = field(metadata={
        'validate': Length(max=20, min=1)
    })
    is_checked: bool = field()
    value: str = field()


@dataclass(frozen=True)
class User(BaseDataclass):
    id: int = field(metadata={
        "strict": True,
    })
    registration_date: datetime = field()
    name: str = field(metadata={
        'validate': Length(max=150)
    })
    discount: int = field(metadata={
        "strict": True,
        "validate": Range(min=0, max=100)
    })
    send_sms: bool = field()
    send_email: bool = field()
    language: str = field(metadata={
        "validate": Length(equal=2)
    })
    currency: str = field(metadata={
        "validate": Length(equal=3)
    })
    is_moderated: bool = field()
    banned: bool = field()
    data: Dict[str, Any] = field(default_factory=dict)
    data_for_auth: Optional[List[DataForAuth]] = field(
        default_factory=list, metadata={
            'validate': UniqueItems(),
        })
    roles: List[str] = field(default_factory=list, metadata={
        'validate': [
            ContainsOnly([role.value for role in Roles]),
            UniqueItems(),
            Filled()
        ],
        'required': True
    })


@dataclass(frozen=True)
class RegistrationUserData(BaseDataclass):
    password: str = field(metadata={"validate": Length(min=6, max=30)})
    phone: Optional[str] = field(metadata={"validate": Phone()})
    email: Optional[str] = field(metadata={"validate": Email()})
    name: Optional[str] = field(metadata={"validate": Length(min=1, max=150)})
    language: str = field(metadata={"validate": Length(equal=2)})
    currency: str = field(metadata={"validate": Length(equal=3)})
    send_sms: bool = field(default=True)
    send_email: bool = field(default=True)

    def __post_init__(self):
        if not self.phone and not self.email:
            raise ValidationError(
                {"_schema": [
                    'You need to fill in at least '
                    'one field from "email" or "phone"'
                ]}
            )


@dataclass(frozen=True)
class ConfirmDataForAuthRequest(BaseDataclass):
    code: str = field(metadata={"validate": Length(min=4, max=20)})


@dataclass(frozen=True)
class UsersResponse(SuccessResponse):
    pager: Pager = field()
    result: List[User] = field(default_factory=list, metadata={
        "required": True
    })


@dataclass(frozen=True)
class ChangePasswordRequest(BaseDataclass):
    old_password: str = field(metadata={"validate": Length(min=6, max=30)})
    new_password: str = field(metadata={"validate": Length(min=6, max=30)})

    def __post_init__(self):
        if self.old_password == self.new_password:
            raise ValidationError(
                {"_schema": [
                    'New password should be different with old password'
                ]}
            )
