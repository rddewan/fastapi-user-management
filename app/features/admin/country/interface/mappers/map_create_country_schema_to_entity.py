

from app.features.admin.country.domain.country_entity import CountryEntity
from app.features.admin.country.interface.schemas import CreateCountryRequest


def mapCreateCountrySchemaToEntity(country_schema: CreateCountryRequest) -> CountryEntity:
    return CountryEntity(
        name=country_schema.name,
        country_code=country_schema.country_code,
        currency_code=country_schema.currency_code
    )
        