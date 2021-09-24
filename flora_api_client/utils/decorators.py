from functools import wraps
from http import HTTPStatus

from flora_api_client.schemas import ErrorResponseSchema
from flora_api_client.schemas import RenewTokenResponseSchema


def expectations(*, schema, expected_code=HTTPStatus.OK):
    def decorate(fn):
        @wraps(fn)
        async def inner(*args, **kwargs):
            code, res, new_tokens = await fn(*args, **kwargs)
            sch = schema() if code == expected_code else ErrorResponseSchema()
            tokens = RenewTokenResponseSchema().load(
                new_tokens
            ) if new_tokens else None
            return code, sch.load(res), tokens
        return inner
    return decorate
