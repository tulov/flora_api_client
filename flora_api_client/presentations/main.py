from dataclasses import dataclass, field


@dataclass(frozen=True)
class ApplicationInfoResponse:
    version: str = field()
    name: str = field()
