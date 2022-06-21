import marshmallow_dataclass
from flora_api_client.presentations.products import (
    ProductResponse, ProductRequest, ProductsResponse, FeaturedProductsResponse,
    FeaturedProductsQuerystring, PreferredExecutorResponse,
    PreferredExecutorQuerystring
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
FeaturedProductsQuerystringSchema = marshmallow_dataclass.class_schema(
    FeaturedProductsQuerystring
)

PreferredExecutorResponseSchema = marshmallow_dataclass.class_schema(
    PreferredExecutorResponse
)

PreferredExecutorQuerystringSchema = marshmallow_dataclass.class_schema(
    PreferredExecutorQuerystring
)
