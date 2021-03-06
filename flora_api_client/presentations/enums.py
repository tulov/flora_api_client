from enum import Enum, unique


@unique
class Roles(Enum):
    user = 'user'
    partner = 'partner'
    admin = 'admin'


@unique
class ModerationAction(Enum):
    user_registration = 'user_registration'
    product = 'product'


@unique
class ModerationResult(Enum):
    approved = 'approved'
    denied = 'denied'


@unique
class ImageTarget(Enum):
    product = 'product'
    menu = 'menu'


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


@unique
class ProgramType(Enum):
    percent = 'percent'
    amount = 'amount'


@unique
class ProgramAction(Enum):
    discount = 'discount'
    markup = 'markup'


@unique
class Currency(Enum):
    usd = 'usd'
    rub = 'rub'
    kzt = 'kzt'
    eur = 'eur'


@unique
class UnitOfWeight(Enum):
    kg = 'kg'
    g = 'g'


@unique
class UnitOfSize(Enum):
    sm = 'sm'
    mm = 'mm'
    m = 'm'


@unique
class UnitOfCount(Enum):
    thing = 'thing'
    meter = 'meter'
    unit = 'unit'


@unique
class OrderState(Enum):
    new = "new"
    payed = "payed"
    accepted = "accepted"
    on_delivery = "on_delivery"
    delivered = "delivered"
    closed = "closed"
    claim = "claim"
    canceled = "canceled"
