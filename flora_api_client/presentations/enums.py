from enum import Enum, unique


@unique
class Roles(Enum):
    user = 'user'
    partner = 'partner'
    admin = 'admin'


@unique
class ModerationAction(Enum):
    user_registration = 'user_registration'


@unique
class ModerationResult(Enum):
    approved = 'approved'
    denied = 'denied'


@unique
class ImageTarget(Enum):
    product = 'product'


@unique
class FieldType(Enum):
    integer = 'integer'
    string = 'string'
    boolean = 'boolean'


@unique
class HTMLWidget(Enum):
    number = 'number'
    string = 'string'
    select = 'select'
    multiselect = 'multiselect'
    checkbox = 'checkbox'
    radio = 'radio'
    textarea = 'textarea'
