from pydantic import BaseModel
from app.features.admin.country.domain.country_entity import CountryEntity

class CountryListResponse(BaseModel):
    status: str
    data: list[CountryEntity]


class CountryResponse(BaseModel):
    status: str
    data: CountryEntity
    