from dataclasses import dataclass, field

from marshmallow.validate import Length


@dataclass(frozen=True)
class AuthRequest:
    auth_key: str = field(metadata={
        'validate': Length(min=3, max=150)
    })
    password: str = field(metadata={
        'validate': Length(min=6, max=30)
    })
