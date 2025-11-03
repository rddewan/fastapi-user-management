from typing import Optional
from pydantic import BaseModel
from app.features.admin.country.domain.country_entity import CountryEntity

class CreateCountryRequest(BaseModel):
    name: str
    country_code: str
    currency_code: str

class UpdateCountryRequest(BaseModel):
    name: Optional[str] = None
    country_code: Optional[str] = None
    currency_code: Optional[str] = None

class PaginationMeta(BaseModel):
    total: int
    total_pages: int
    page_size: int
    current_page: int
    
    

class CountryListResponse(BaseModel):
    status: str
    data: list[CountryEntity]
    meta: PaginationMeta


class CountryResponse(BaseModel):
    status: str
    data: CountryEntity
    