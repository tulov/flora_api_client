import re

import typing

from marshmallow import ValidationError
from marshmallow.validate import Validator


class Phone(Validator):
    """Validate an phone.

    :param error: Error message to raise in case of a validation error. Can be
        interpolated with `{input}`.
    """

    PHONE_REGEX = re.compile(
        r"[0-9]{11,15}",
    )

    default_message = "Not a valid phone number."

    def __init__(self, *, error: typing.Optional[str] = None):
        self.error = error or self.default_message  # type: str

    def _format_error(self, value: str) -> str:
        return self.error.format(input=value)

    def __call__(self, value: str) -> str:
        message = self._format_error(value)

        if not value:
            raise ValidationError(message)

        if not self.PHONE_REGEX.match(value):
            raise ValidationError(message)

        return value


class UniqueItems(Validator):
    def __init__(self, *, message='items must be unique'):
        self._message = message

    def __call__(
        self, value: typing.Union[typing.List, typing.Tuple]
    ) -> typing.Union[typing.List, typing.Tuple]:
        if not value:
            return value
        if len(value) != len(set(value)):
            raise ValidationError(self._message)
        return value


class Filled(Validator):
    def __init__(self, *, message='container should be filled'):
        self._message = message

    def __call__(
        self, value: typing.Union[typing.List, typing.Tuple]
    ) -> typing.Union[typing.List, typing.Tuple]:
        if not value:
            raise ValidationError(self._message)
        return value