from functools import wraps
from http import HTTPStatus
from marshmallow import EXCLUDE

from flora_api_client.schemas import ErrorResponseSchema
from flora_api_client.schemas import RenewTokenResponseSchema
from flora_api_client.schemas import OrderResponseSchema


def expectations(*, schema, expected_code=HTTPStatus.OK):
    def decorate(fn):
        @wraps(fn)
        async def inner(*args, **kwargs):
            code, res, new_tokens = await fn(*args, **kwargs)
            sch = schema() if code == expected_code else ErrorResponseSchema()
            tokens = RenewTokenResponseSchema().load(
                new_tokens, unknown=EXCLUDE
            ) if new_tokens else None
            if schema == OrderResponseSchema:
                o = sch.load(res, unknown=EXCLUDE)
                for i in range(0, len(o.children)):
                    o.children[i] = sch.load(o.children[i], unknown=EXCLUDE)
                return code, o, tokens
            return code, sch.load(res, unknown=EXCLUDE), tokens
        return inner
    return decorate
