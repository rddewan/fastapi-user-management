from typing import Optional

from sqlalchemy.orm.mapper import Mapper
from sqlalchemy.orm.query import inspect
from app.features.admin.country.domain.country_entity import CountryEntity
from app.features.admin.country.infrastructure.models.country_model import CountryModel

def map_entity_to_country_model(
    entity: CountryEntity, 
    model: Optional[CountryModel] = None,
) -> CountryModel:
    """
    Map a CountryEntity to a CountryModel.

    Args:
        entity (CountryEntity): The CountryEntity to map.

    Returns:
        CountryModel: The mapped CountryModel.
    """
    if model is None:
        return CountryModel(
            id=entity.id,
            name=entity.name,
            country_code=entity.country_code,
            currency_code=entity.currency_code,
            created_at=entity.created_at,
            updated_at=entity.updated_at,
        )
    else:
        mapper: Mapper[CountryModel] = inspect(CountryModel)
        # extract the column names
        column_names =  [ cols.key for cols in mapper.column_attrs]
        print(f"Column names: {column_names}")

        # extract the primary keys
        primary_keys = [cols.key for cols in mapper.primary_key]
        print(f"Primary keys: {primary_keys}")
        
        # skip the primary keys and created_at and updated_at columns
        skip = primary_keys + ["created_at", "updated_at"]

        for column in column_names:
            if column in skip:
                continue
            if hasattr(entity, column):
                value = getattr(entity, column)
                if value is not None:
                    setattr(model, column, value)

        return model