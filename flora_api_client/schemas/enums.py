from enum import Enum, unique


@unique
class Roles(Enum):
    user = 'user'
    partner = 'partner'
    admin = 'admin'
