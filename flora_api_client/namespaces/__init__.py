from .users import UsersNamespace
from .info import InfoNamespace
from .partners import PartnersNamespace
from .auth import AuthNamespace
from .data_for_auth import DataForAuthNamespace
from .counters import CountersNamespace


NAMESPACES = {
    "users": UsersNamespace,
    'info': InfoNamespace,
    'partners': PartnersNamespace,
    'auth': AuthNamespace,
    'data_for_auth': DataForAuthNamespace,
    'counters': CountersNamespace,
}
