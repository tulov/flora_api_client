from .users import UsersNamespace
from .info import InfoNamespace
from .partners import PartnersNamespace
from .auth import AuthNamespace


NAMESPACES = {
    "users": UsersNamespace,
    'info': InfoNamespace,
    'partners': PartnersNamespace,
    'auth': AuthNamespace,
}
