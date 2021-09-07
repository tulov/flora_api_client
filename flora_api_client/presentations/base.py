from dataclasses import asdict, dataclass, field
from typing import Optional


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


@dataclass(frozen=True)
class Querystring(BaseDataclass):
    f: Optional[str] = field()  # фильтр
    w: Optional[str] = field()  # добавочные поля, через запятую
    p: Optional[int] = field()  # страница
    s: Optional[str] = field()  # сортировка
