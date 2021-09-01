from dataclasses import dataclass, field
from typing import Dict, Any, Optional


@dataclass(frozen=True)
class Error:
    code: str = field()
    message: str = field()
    error_code: Optional[int] = field()
    fields: Dict[str, Any] = field(default_factory=dict)


class ErrorResponse:
    error: Error = field()
