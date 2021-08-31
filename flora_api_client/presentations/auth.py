from dataclasses import dataclass, field

from marshmallow.validate import Length
from .users import User


@dataclass(frozen=True)
class AuthRequest:
    auth_key: str = field(metadata={
        'validate': Length(min=3, max=150)
    })
    password: str = field(metadata={
        'validate': Length(min=6, max=30)
    })


@dataclass(frozen=True)
class AuthResponse:
    token: str = field()
    user: User = field()
