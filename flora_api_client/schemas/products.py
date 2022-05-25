import marshmallow_dataclass
from flora_api_client.presentations.products import (
    ProductResponse, ProductRequest, ProductsResponse, FeaturedProductsResponse
)


ProductResponseSchema = marshmallow_dataclass.class_schema(
    ProductResponse
)
ProductsResponseSchema = marshmallow_dataclass.class_schema(
    ProductsResponse
)
ProductRequestSchema = marshmallow_dataclass.class_schema(
    ProductRequest
)
FeaturedProductsResponseSchema = marshmallow_dataclass.class_schema(
    FeaturedProductsResponse
)
