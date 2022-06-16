from flora_api_client.auth.singer import Singer
from flora_api_client.namespaces import (
    NAMESPACES, UsersNamespace, AuthNamespace, InfoNamespace, PartnersNamespace,
    DataForAuthNamespace, CountersNamespace, ModerationNamespace,
    CategoriesNamespace, TagsNamespace, FieldsNamespace, ImagesNamespace,
    ProductsNamespace, CitiesNamespace, PricesNamespace, ProgramsNamespace,
    MenuNamespace, SliderItemsNamespace
)


class FloraApiClient:
    users: UsersNamespace
    auth: AuthNamespace
    info: InfoNamespace
    partners: PartnersNamespace
    data_for_auth: DataForAuthNamespace
    counters: CountersNamespace
    moderation: ModerationNamespace
    categories: CategoriesNamespace
    tags: TagsNamespace
    fields: FieldsNamespace
    images: ImagesNamespace
    products: ProductsNamespace
    cities: CitiesNamespace
    prices: PricesNamespace
    programs: ProgramsNamespace
    menu: MenuNamespace
    slider_items: SliderItemsNamespace

    def __init__(self, *, app_id: str, app_key: str,
                 host: str, url_prefix: str = '/api/v1'):
        signer = Singer(private_key=app_key, public_key=app_id)
        self._namespaces = {}
        for name, ns in NAMESPACES.items():
            setattr(self, name, ns(host, url_prefix, signer))
