from dataclasses import asdict, dataclass, field


@dataclass(frozen=True)
class BaseDataclass:
    def as_dict(self):
        return asdict(self)


@dataclass(frozen=True)
class SuccessResponse(BaseDataclass):
    success: bool = field()
