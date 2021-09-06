from dataclasses import dataclass, field, asdict

from marshmallow.validate import Length
from .users import User
from .base import BaseDataclass


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
