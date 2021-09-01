from dataclasses import dataclass, field
from typing import Dict, Any, Optional
from .base import BaseDataclass


@dataclass(frozen=True)
class Error(BaseDataclass):
    code: str = field()
    message: str = field()
    error_code: Optional[int] = field()
    fields: Dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class ErrorResponse(BaseDataclass):
    error: Error = field()
