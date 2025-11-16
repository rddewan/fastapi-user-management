
from typing import Optional
from app.core.exceptions.repository import UniqueConstraintFailure
from app.features.admin.country.application.interface.icountry_repository import (ICountryRepository)
from app.features.admin.country.domain.country_entity import CountryEntity
from app.features.admin.country.domain.exceptions.exception import CountryAlreadyExistsException

class CountryService:

    def __init__(self, repository: ICountryRepository):
        self.repository = repository

    def get_all_countries(self, skip: int, limit: int, search: Optional[str] = None) -> tuple[list[CountryEntity], int, int]:
        """Get all the countries

        Returns:
            list[CountryEntity]: this will return a list of the CountryEntity
        """

        return self.repository.get_all_countries(skip, limit, search)

    def get_country_by_id(self, country_id: int) -> CountryEntity:
        """Get a country by ID

        Args:
            country_id (int): ID of the country to get

        Returns:
            CountryEntity: The country if found
        """
        return self.repository.get_country_by_id(country_id)

    def create_country(self, country: CountryEntity) -> CountryEntity:
        try:

            """Create a new country

            Args:
                country (CountryEntity): The country data to create

            Returns:
                CountryEntity: The created country
            """
            return self.repository.create_country(country)
        except UniqueConstraintFailure:
            raise CountryAlreadyExistsException(entity="Country", key=country.name)

    def update_country(self, country_id: int, country: CountryEntity) -> CountryEntity:
        try:
            """Update existing country

            Args:
                country_id (int): ID of the country to update
                country (CountryEntity): Country data to update

            Returns:
                CountryEntity: THe updated country
            """
            return self.repository.update_country(country_id, country)
        except UniqueConstraintFailure:
            raise CountryAlreadyExistsException(entity="Country", key=country.name)

    def delete_country(self, country_id: int) -> bool:
        """Delete a country

        Args:
            country_id (int): ID of the country to delete

        Returns:
            bool: True if the country was deleted, False otherwise
        """
        return self.repository.delete_country(country_id)
