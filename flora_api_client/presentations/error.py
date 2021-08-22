from dataclasses import dataclass, field
from typing import Dict, Any


@dataclass(frozen=True)
class Error:
    code: str = field()
    message: str = field()
    fields: Dict[str, Any] = field(default_factory=dict)


class ErrorResponse:
    error: Error = field()
