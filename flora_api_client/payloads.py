import json
from datetime import date, datetime
from decimal import Decimal
from functools import partial, singledispatch
from typing import Any
from enum import Enum
from uuid import UUID

from aiohttp.payload import JsonPayload as BaseJsonPayload, Payload
from aiohttp.typedefs import JSONEncoder
from asyncpg import Record
from flora_api_client.presentations.base import BaseDataclass

from flora_api_client.schemas import DATE_FORMAT, DATETIME_FORMAT


@singledispatch
def convert(value):
    """
    Модуль json позволяет указать функцию, которая будет вызываться для
    обработки не сериализуемых в JSON объектов. Функция должна вернуть либо
    сериализуемое в JSON значение, либо исключение TypeError:
    https://docs.python.org/3/library/json.html#json.dump
    """
    raise TypeError(f"Unserializable value: {value!r}")


@convert.register(Enum)
def convert_enum(value: Enum):
    return value.value


@convert.register(BaseDataclass)
def convert_dataclass(value: BaseDataclass):
    return value.as_dict()


@convert.register(UUID)
def convert_uuid(value: UUID):
    return str(value)


@convert.register(Record)
def convert_asyncpg_record(value: Record):
    """
    Позволяет автоматически сериализовать результаты запроса, возвращаемые
    asyncpg.
    """
    return dict(value)


@convert.register(date)
def convert_date(value: date):
    """
    В проекте объект date возвращается только в одном случае - если необходимо
    отобразить дату рождения. Для отображения даты рождения должен
    использоваться формат ДД.ММ.ГГГГ.
    """
    return value.strftime(DATE_FORMAT)


@convert.register(datetime)
def convert_datetime(value: datetime):
    return value.strftime(DATETIME_FORMAT)


@convert.register(Decimal)
def convert_decimal(value: Decimal):
    """
    asyncpg возвращает округленные перцентили возвращаются виде экземпляров
    класса Decimal.
    """
    return float(value)


dumps = partial(json.dumps, default=convert, ensure_ascii=False)


class JsonPayload(BaseJsonPayload):
    """
    Заменяет функцию сериализации на более "умную" (умеющую упаковывать в JSON
    объекты asyncpg.Record и другие сущности).
    """

    def __init__(
        self,
        value: Any,
        encoding: str = "utf-8",
        content_type: str = "application/json",
        dumps: JSONEncoder = dumps,
        *args: Any,
        **kwargs: Any,
    ) -> None:
        super().__init__(value, encoding, content_type, dumps, *args, **kwargs)

    def decode(self, encoding: str) -> str:
        return self._value.decode(encoding)


class AsyncGenJSONListPayload(Payload):
    """
    Итерируется по объектам AsyncIterable, частями сериализует данные из них
    в JSON и отправляет клиенту.
    """

    def __init__(
        self,
        value,
        encoding: str = "utf-8",
        content_type: str = "application/json",
        root_object: str = "data",
        *args,
        **kwargs,
    ):
        self.root_object = root_object
        super().__init__(
            value, content_type=content_type, encoding=encoding, *args, **kwargs
        )

    async def write(self, writer):
        # Начало объекта
        await writer.write(('{"%s":[' % self.root_object).encode(self._encoding))

        first = True
        async for row in self._value:
            # Перед первой строчкой запятая не нужнаа
            if not first:
                await writer.write(b",")
            else:
                first = False

            await writer.write(dumps(row).encode(self._encoding))

        # Конец объекта
        await writer.write(b"]}")


__all__ = (
    "JsonPayload",
    "AsyncGenJSONListPayload",
    "convert_date",
    "convert_enum",
    "convert_uuid",
    "convert_decimal",
    "convert_datetime",
    "dumps",
)
