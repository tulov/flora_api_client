import marshmallow_dataclass
from flora_api_client.presentations.cities import (
    CityResponse, CitiesResponse, SearchCitiesResponse
)


CityResponseSchema = marshmallow_dataclass.class_schema(
    CityResponse
)
CitiesResponseSchema = marshmallow_dataclass.class_schema(
    CitiesResponse
)
SearchCitiesResponseSchema = marshmallow_dataclass.class_schema(
    SearchCitiesResponse
)
