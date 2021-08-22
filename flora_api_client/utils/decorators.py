from functools import wraps
from http import HTTPStatus

from flora_api_client.schemas import ErrorResponseSchema


def expectations(*, schema, expected_code=HTTPStatus.OK):
    def decorate(fn):
        @wraps(fn)
        async def inner(*args, **kwargs):
            code, res = await fn(*args, **kwargs)
            sch = schema() if code == expected_code else ErrorResponseSchema()
            return code, sch.load(res)
        return inner
    return decorate
