from marshmallow import Schema
from marshmallow.fields import Str


class ApplicationInfoResponseSchema(Schema):
    version = Str(required=True)
    name = Str(required=True)
