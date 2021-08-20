from marshmallow import Schema, validates, ValidationError, validates_schema
from marshmallow.fields import Str, Integer, List, DateTime, Bool, Dict, Nested
from marshmallow.validate import Length, Range, ContainsOnly, Email
from .enums import Roles
from .validates import Phone


class DataForAuthSchema(Schema):
    id = Integer(required=True, strict=True)
    service = Str(required=True)
    is_checked = Bool(required=True)
    value = Str(required=True)


class UserSchema(Schema):
    id = Integer(required=True, strict=True)
    roles = List(Str(), required=True,
                 validate=ContainsOnly([role.value for role in Roles]))
    registration_date = DateTime(required=True)
    name = Str(required=True, validate=Length(max=150))
    discount = Integer(strict=True, required=True,
                       validate=Range(min=0, max=100))
    send_sms = Bool(required=True)
    send_email = Bool(required=True)
    language = Str(required=True,
                   validate=Length(equal=2))
    currency = Str(required=True,
                   validate=Length(equal=3))
    is_moderated = Bool(required=True)
    data_for_auth = Nested(DataForAuthSchema, many=True, required=True)
    data = Dict(required=False)

    @validates('roles')
    def validate_roles(self, value: list):
        if len(value) != len(set(value)):
            raise ValidationError('roles must be unique')


class RegistrationUserSchema(Schema):
    password = Str(required=True,
                   validate=Length(min=6, max=30))
    phone = Str(required=False, validate=Phone())
    email = Str(required=False, validate=Email())
    name = Str(required=False, validate=Length(min=1, max=150))
    send_sms = Bool(required=False, default=True)
    send_email = Bool(required=False, default=True)
    language = Str(required=True, validate=Length(equal=2))
    currency = Str(required=True, validate=Length(equal=3))

    @validates_schema(skip_on_field_errors=True)
    def validate_object(self, data, **kwargs):
        if 'email' not in data and 'phone' not in data:
            raise ValidationError(
                'You need to fill in at least one field from "email" or "phone"'
            )
