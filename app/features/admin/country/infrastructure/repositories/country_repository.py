from typing import override
from app.features.admin.country.application.interface.icountry_repository import (
    ICountryRepository,
)
from sqlalchemy.orm import Session
from app.features.admin.country.domain.country_entity import CountryEntity
from app.features.admin.country.infrastructure.models.country_model import CountryModel
from app.features.admin.country.infrastructure.mappers.map_country_entity_to_country_model import (
    map_country_entity_to_country_model,
)
from app.features.admin.country.infrastructure.mappers.map_country_model_to_country_entity import (
    map_country_model_to_country_entity,
)


class CountryRepository(ICountryRepository):

    def __init__(self, session: Session):
        self.session: Session = session

    @override
    def get_all_countries(self) -> list[CountryEntity]:
        """
        Get all countries

        Returns:
            list[CountryEntity]: List of country entities
        """
        countries = self.session.query(CountryModel).all()
        # Map country model to country entity
        result = [map_country_model_to_country_entity(country) for country in countries]
        # Return list of country entities
        return result

    @override
    def get_country_by_id(self, country_id: int) -> CountryEntity:
        """
        Get country by id

        Args:
            country_id (int): Country id

        Returns:
            CountryEntity: Country entity
        """
        result = (
            self.session.query(CountryModel)
            .filter(CountryModel.id == country_id)
            .first()
        )
        return map_country_model_to_country_entity(result)

    @override
    def create_country(self, country: CountryEntity) -> CountryEntity:
        """
        Create country

        Args:
            country (CountryEntity): Country entity

        Returns:
            CountryEntity: Country entity
        """

        # Map country entity to country model
        country_model = map_country_entity_to_country_model(country)
        # Add country model to session
        self.session.add(country_model)
        # Commit session
        self.session.commit()
        # Map country model to country entity and return
        return map_country_model_to_country_entity(country_model)

    @override
    def update_country(self, country_id: int, country: CountryEntity) -> CountryEntity:
        """
        Update country

        Args:
            country_id (int): Country id
            country (CountryEntity): Country entity

        Returns:
            CountryEntity: Country entity
        """

        # Get country by id
        country_model = (
            self.session.query(CountryModel)
            .filter(CountryModel.id == country_id)
            .first()
        )
        # TODO: raise exception if country is not found

        # Map country entity to country model
        country_model = map_country_entity_to_country_model(country, country_model)        
        # Commit session
        self.session.commit()
        # Map country model to country entity and return
        return map_country_model_to_country_entity(country_model)

    @override
    def delete_country(self, country_id: int) -> bool:
        """
        Delete country

        Args:
            country_id (int): Country id
        """
        # Get country by id
        country_model = (
            self.session.query(CountryModel)
            .filter(CountryModel.id == country_id)
            .first()
        )
        # TODO: raise exception if country is not found

        # Delete country model
        self.session.delete(country_model)
        # Commit session
        self.session.commit()
        # Return true
        return True
