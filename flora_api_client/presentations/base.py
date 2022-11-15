from dataclasses import asdict, dataclass, field
from typing import Optional, Any


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
    count_objects: Optional[int] = field()
    page: int = field(default=1)
    per_page: int = field(default=10)

    @staticmethod
    def _split_diapasons(diapason1, diapason2):
        if set(diapason1) & set(diapason2) or diapason1[
            len(diapason1) - 1
        ] + 1 == diapason2[0]:
            for x in diapason2:
                if x not in diapason1:
                    diapason1.append(x)
        elif len(diapason2):
            diapason1.append('.')
            for x in diapason2:
                diapason1.append(x)
        return diapason1

    def get_visible_pages(self):
        if self.count_pages == 0:
            return []
        diapason1 = [1, 2]
        diapason2 = [self.page - 1, self.page, self.page + 1]
        diapason3 = [self.count_pages - 1, self.count_pages]

        # в каждом диапазоне убираем все, что больше чем количество страниц
        # и меньше чем 1
        diapason1 = [x for x in diapason1 if x <= self.count_pages]
        diapason2 = [x for x in diapason2 if 0 < x <= self.count_pages]
        diapason3 = [x for x in diapason3 if 0 < x <= self.count_pages]

        # объединяем диапазоны
        diapason1 = self._split_diapasons(diapason1, diapason2)
        diapason1 = self._split_diapasons(diapason1, diapason3)
        return diapason1


@dataclass(frozen=True)
class WithFieldsQuerystring(BaseDataclass):
    with_fields: Optional[str] = field()  # добавочные поля, через запятую


@dataclass(frozen=True)
class Querystring(WithFieldsQuerystring):
    # фильтр. Допускает сложные условия.
    # Например: action:test|one|two,result:req
    # action in (test, one, two) and result in (req)
    filters: Optional[str] = field()  # фильтр
    sorts: Optional[str] = field()  # сортировка
    page: Optional[int] = field(default=1)  # страница
    per_page: Optional[int] = field(
        default=10)  # количество элементов на странице


@dataclass(frozen=True)
class PagedResponse(SuccessResponse):
    pager: Optional[Pager] = field()


@dataclass(frozen=True)
class ResultResponse(SuccessResponse):
    result: Any = field()


@dataclass(frozen=True)
class DataRequest(BaseDataclass):
    data: Any = field()


@dataclass(frozen=True)
class RevisionRequest(BaseDataclass):
    revision: int = field(metadata={
        "strict": True
    })
