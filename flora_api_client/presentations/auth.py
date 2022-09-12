from dataclasses import dataclass, field

from marshmallow.validate import Length, OneOf
from .users import User
from .base import BaseDataclass
from .enums import CommunicationTransports


@dataclass(frozen=True)
class AuthRequest(BaseDataclass):
    auth_key: str = field(metadata={
        'validate': Length(min=3, max=150)
    })
    password: str = field(metadata={
        'validate': Length(min=6, max=30)
    })


@dataclass(frozen=True)
class AuthResponse(BaseDataclass):
    token: str = field()
    long_token: str = field()
    user: User = field()


@dataclass(frozen=True)
class RenewTokenRequest(BaseDataclass):
    token: str = field()


@dataclass(frozen=True)
class RenewTokenResponse(BaseDataclass):
    token: str = field()
    long_token: str = field()


@dataclass(frozen=True)
class SendRestoreAccessLinkRequest(BaseDataclass):
    auth_key: str = field(metadata={
        'validate': Length(min=3, max=150)
    })


@dataclass(frozen=True)
class RestoreAccessRequest(BaseDataclass):
    token: str = field()
    password: str = field(metadata={
        'validate': Length(min=6, max=30)
    })


@dataclass(frozen=True)
class EnterCodeRequest(BaseDataclass):
    auth_key: str = field(metadata={
        'validate': Length(min=3, max=150)
    })
    transport: str = field(metadata={
        "validate": OneOf([r.value for r in CommunicationTransports])
    })


@dataclass(frozen=True)
class AuthCodeRequest(BaseDataclass):
    auth_key: str = field(metadata={
        'validate': Length(min=3, max=150)
    })
    code: str = field(metadata={
        'validate': Length(equal=4)
    })
