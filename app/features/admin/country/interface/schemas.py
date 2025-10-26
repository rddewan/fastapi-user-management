from pydantic import BaseModel, Field
from app.features.admin.country.domain.country_entity import CountryEntity


class CountryCreate(BaseModel):
    name: str = Field(..., min_length=3, max_length=100)
    country_code: str = Field(..., min_length=1, max_length=3)
    currency_code: str = Field(..., min_length=1, max_length=10)


class CountryListResponse(BaseModel):
    status: str
    data: list[CountryEntity]


class CountryResponse(BaseModel):
    status: str
    data: CountryEntity
    