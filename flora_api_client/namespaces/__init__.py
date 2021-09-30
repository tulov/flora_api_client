from .users import UsersNamespace
from .info import InfoNamespace
from .partners import PartnersNamespace
from .auth import AuthNamespace
from .data_for_auth import DataForAuthNamespace
from .counters import CountersNamespace
from .moderation import ModerationNamespace
from .categories import CategoriesNamespace


NAMESPACES = {
    "users": UsersNamespace,
    'info': InfoNamespace,
    'partners': PartnersNamespace,
    'auth': AuthNamespace,
    'data_for_auth': DataForAuthNamespace,
    'counters': CountersNamespace,
    'moderation': ModerationNamespace,
    'categories': CategoriesNamespace,
}
