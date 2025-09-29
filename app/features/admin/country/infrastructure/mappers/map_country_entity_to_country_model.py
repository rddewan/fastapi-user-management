from app.features.admin.country.domain.country_entity import CountryEntity
from app.features.admin.country.infrastructure.models.country_model import CountryModel

def map_country_entity_to_country_model(entity: CountryEntity) -> CountryModel:
    """
    Map a CountryEntity to a CountryModel.

    Args:
        entity (CountryEntity): The CountryEntity to map.

    Returns:
        CountryModel: The mapped CountryModel.
    """
    return CountryModel(
        id=entity.id,
        name=entity.name,
        country_code=entity.country_code,
        currency_code=entity.currency_code,
        created_at=entity.created_at,
        updated_at=entity.updated_at,
    )