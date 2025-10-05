
from abc import ABC, abstractmethod
from app.features.admin.country.domain.country_entity import CountryEntity

class ICountryRepository(ABC):
    """
    Interface for country repository
    """

    @abstractmethod
    def get_all_countries(self) -> list[CountryEntity]:
        """
        Get all countries
        """
        pass

    @abstractmethod
    def get_country_by_id(self, country_id: int) -> CountryEntity:
        """
        Get country by id
        """
        pass

    @abstractmethod
    def create_country(self, country: CountryEntity) -> CountryEntity:
        """
        Create country
        """
        pass
    
    @abstractmethod
    def update_country(self, country_id: int, country: CountryEntity) -> CountryEntity:
        """
        Update country
        """
        pass
    
    @abstractmethod
    def delete_country(self, country_id: int) -> None:
        """
        Delete country
        """
        pass
    
    