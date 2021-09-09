from dataclasses import dataclass, field
from .base import SuccessResponse, BaseDataclass


@dataclass(frozen=True)
class CountersResult(BaseDataclass):
    moderate: int = field(default=0)


@dataclass(frozen=True)
class CountersResponse(SuccessResponse):
    result: CountersResult = field()
