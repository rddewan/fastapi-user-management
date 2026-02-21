import math
from typing import Optional, override

from sqlalchemy import func, or_
from sqlalchemy.exc import IntegrityError, OperationalError, SQLAlchemyError
from app.core.exceptions.repository import ConnectionFailure, RepositoryException, TransactionFailure, UniqueConstraintFailure
from app.features.admin.country.application.interface.icountry_repository import (
    ICountryRepository,
)
from sqlalchemy.orm import Session
from app.features.admin.country.domain.country_entity import CountryEntity
from app.features.admin.country.domain.exceptions.exception import CountryNotFoundException
from app.features.admin.country.infrastructure.models.country_model import CountryModel
from app.features.admin.country.infrastructure.mappers.map_entity_to_country_model import (
    map_entity_to_country_model,
)
from app.features.admin.country.infrastructure.mappers.map_country_model_to_entity import (
    map_country_model_to_entity,
)


class CountryRepository(ICountryRepository):

    def __init__(self, session: Session):
        self.session: Session = session

    @override
    def get_all_countries(self, skip: int, limit: int, search: Optional[str] = None) -> tuple[list[CountryEntity], int, int]:
        try:
            """
            Get all countries

            Returns:
                list[CountryEntity]: List of country entities
            """

            # base query
            query = self.session.query(CountryModel)

            # search  by name, country_code, currency_code
            if search:
                pattern = f"%{search}%"
                query = query.filter(
                    or_(
                        CountryModel.name.ilike(pattern),
                        CountryModel.country_code.ilike(pattern),
                        CountryModel.currency_code.ilike(pattern)
                    )
                )
            
            # sort by the name in asc, then paginate
            countries = (
                query
                .order_by(CountryModel.name.asc())
                .offset(skip)
                .limit(limit)
                .all()
            )

            # count all the record by id
            total = query.with_entities(func.count(CountryModel.id)).scalar() or 0

            # total pages
            total_pages = math.ceil(total / limit) if limit > 0 else 1
            
            # Map country model to country entity
            result = [map_country_model_to_entity(country) for country in countries]
            # Return list of country entities
            return result, total, total_pages
        except OperationalError as e:
            raise ConnectionFailure() from e
        except SQLAlchemyError as e:
            raise TransactionFailure() from e
        except Exception as e:
            raise RepositoryException() from e

    @override
    def get_country_by_id(self, country_id: int) -> CountryEntity:
        try:

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
            # raise exception if country is not found
            if result is None:
                raise CountryNotFoundException(entity="Country", key=country_id)

            return map_country_model_to_entity(result)
        except OperationalError as e:
            raise ConnectionFailure() from e
        except SQLAlchemyError as e:
            raise TransactionFailure() from e
        

    @override
    def create_country(self, country: CountryEntity) -> CountryEntity:
        try:

            """
            Create country

            Args:
                country (CountryEntity): Country entity

            Returns:
                CountryEntity: Country entity
            """

            # Map country entity to country model
            country_model = map_entity_to_country_model(country)
            # Add country model to session
            self.session.add(country_model)
            # Commit session
            self.session.commit()
            # Map country model to country entity and return
            return map_country_model_to_entity(country_model)
        except IntegrityError as e:
            self.session.rollback()
            raise UniqueConstraintFailure() from e
        except OperationalError as e:
            self.session.rollback()
            raise ConnectionFailure() from e
        except SQLAlchemyError as e:
            self.session.rollback()
            raise TransactionFailure() from e
        except Exception as e:
            self.session.rollback()
            raise RepositoryException() from e

    @override
    def update_country(self, country_id: int, country: CountryEntity) -> CountryEntity:
        try:

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
            country_model = map_entity_to_country_model(country, country_model)        
            # Commit session
            self.session.commit()
            # Map country model to country entity and return
            return map_country_model_to_entity(country_model)
        except IntegrityError as e:
            self.session.rollback()
            raise UniqueConstraintFailure() from e
        except OperationalError as e:
            self.session.rollback()
            raise ConnectionFailure() from e
        except SQLAlchemyError as e:
            self.session.rollback()
            raise TransactionFailure() from e
        except Exception as e:
            self.session.rollback()
            raise RepositoryException() from e

    @override
    def delete_country(self, country_id: int) -> bool:
        try:

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
            
            if country_model is None:
                raise CountryNotFoundException(entity="Country", key=country_id)

            # Delete country model
            self.session.delete(country_model)
            # Commit session
            self.session.commit()
            # Return true
            return True
        except OperationalError as e:
            self.session.rollback()
            raise ConnectionFailure() from e
        except SQLAlchemyError as e:
            self.session.rollback()
            raise TransactionFailure() from e
        
