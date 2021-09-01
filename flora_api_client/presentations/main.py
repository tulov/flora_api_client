from dataclasses import dataclass, field
from .base import BaseDataclass


@dataclass(frozen=True)
class ApplicationInfoResponse(BaseDataclass):
    version: str = field()
    name: str = field()
