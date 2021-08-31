from flora_api_client.auth.singer import Singer
from flora_api_client.namespaces import (
    NAMESPACES, UsersNamespace, AuthNamespace, InfoNamespace, PartnersNamespace
)


class FloraApiClient:
    users: UsersNamespace
    auth: AuthNamespace
    info: InfoNamespace
    partners: PartnersNamespace

    def __init__(self, *, app_id: str, app_key: str,
                 host: str, url_prefix: str = '/api/v1'):
        signer = Singer(private_key=app_key, public_key=app_id)
        self._namespaces = {}
        for name, ns in NAMESPACES.items():
            setattr(self, name, ns(host, url_prefix, signer))
