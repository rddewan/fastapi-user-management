

from app.features.admin.country.domain.country_entity import CountryEntity
from app.features.admin.country.interface.schemas import  UpdateCountryRequest


def mapUpdateCountrySchemaToEntity(country_schema: UpdateCountryRequest) -> CountryEntity:
    return CountryEntity(
        name=country_schema.name,
        country_code=country_schema.country_code,
        currency_code=country_schema.currency_code
    )
        