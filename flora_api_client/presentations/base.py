from dataclasses import asdict, dataclass, field


@dataclass(frozen=True)
class BaseDataclass:
    def as_dict(self):
        return asdict(self)


@dataclass(frozen=True)
class SuccessResponse(BaseDataclass):
    success: bool = field()


@dataclass(frozen=True)
class Pager(BaseDataclass):
    count_pages: int = field()
    page: int = field(default=1)
    per_page: int = field(default=10)
