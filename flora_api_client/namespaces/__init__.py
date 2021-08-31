from .users import UsersNamespace
from .info import InfoNamespace
from .partners import PartnersNamespace


NAMESPACES = {
    "users": UsersNamespace,
    'info': InfoNamespace,
    'partners': PartnersNamespace,
}
