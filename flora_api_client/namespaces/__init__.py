from .users import UsersNamespace
from .info import InfoNamespace
from .partners import PartnersNamespace
from .auth import AuthNamespace
from .data_for_auth import DataForAuthNamespace
from .counters import CountersNamespace
from .moderation import ModerationNamespace
from .categories import CategoriesNamespace
from .tags import TagsNamespace
from .fields import FieldsNamespace


NAMESPACES = {
    "users": UsersNamespace,
    'info': InfoNamespace,
    'partners': PartnersNamespace,
    'auth': AuthNamespace,
    'data_for_auth': DataForAuthNamespace,
    'counters': CountersNamespace,
    'moderation': ModerationNamespace,
    'categories': CategoriesNamespace,
    'tags': TagsNamespace,
    'fields': FieldsNamespace,
}
