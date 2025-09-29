from app.features.admin.country.domain.country_entity import CountryEntity
from app.features.admin.country.infrastructure.models.country_model import CountryModel

def map_country_model_to_country_entity(model: CountryModel) -> CountryEntity:
    """
    Map a CountryModel to a CountryEntity.

    Args:
        model (CountryModel): The CountryModel to map.

    Returns:
        CountryEntity: The mapped CountryEntity.
    """
    return CountryEntity(
        id=model.id,
        name=model.name,
        country_code=model.country_code,
        currency_code=model.currency_code,
        created_at=model.created_at,
        updated_at=model.updated_at,
    )