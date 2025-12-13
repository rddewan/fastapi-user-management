import math
from typing import Optional, override
from sqlalchemy import func, or_
from sqlalchemy.exc import IntegrityError, OperationalError, SQLAlchemyError
from sqlalchemy.orm import Session
from app.core.exceptions.repository import (
    ConnectionFailure,
    RepositoryException,
    TransactionFailure,
    UniqueConstraintFailure,
)
from app.features.shared.user.application.interface.iuser_repository import (
    IUserRepository,
)
from app.features.shared.user.domain.exceptions.exception import UserNotFound
from app.features.shared.user.domain.user_entity import UserEntity
from app.features.shared.user.infrastructure.mappers.map_entity_to_user_model import (
    map_entity_to_user_model,
)
from app.features.shared.user.infrastructure.mappers.map_user_model_to_entity import (
    map_user_model_to_entity,
)
from app.features.shared.user.infrastructure.models.user_model import UserModel


class UserRepository(IUserRepository):

    def __init__(self, session: Session) -> None:
        self.session = session

    @override
    def get_all(
        self, skip: int, limit: int, search: Optional[str] = None
    ) -> tuple[list[UserEntity], int, int]:
        try:
            # base query
            query = self.session.query(UserModel)

            # search query
            if search:
                pattern = f"%{search}%"
                query = query.filter(
                    or_(
                        UserModel.full_name.ilike(f"%{pattern}%"),
                        UserModel.email.ilike(f"%{pattern}%"),
                        UserModel.username.ilike(f"%{pattern}%"),
                    )
                )

            # sort the user ascending by full name
            users = (
                query.order_by(UserModel.full_name.asc())
                .offset(skip)
                .limit(limit)
                .all()
            )

            # count the total record
            total = query.with_entities(func.count(UserModel.id)).scalar() or 0

            # total pages
            total_pages = math.ceil(total / limit) if limit > 0 else 1

            result = [map_user_model_to_entity(user) for user in users]
            return result, total, total_pages
        except OperationalError as e:
            raise ConnectionFailure() from e
        except SQLAlchemyError as e:
            raise TransactionFailure() from e
        except Exception as e:
            raise RepositoryException() from e

    @override
    def get_by_id(self, id: int) -> UserEntity:
        try:
            result = self.session.query(UserModel).filter(UserModel.id == id).first()

            # raise the exception if user is not found
            if result is None:
                raise UserNotFound(entity="User", key="id")

            return map_user_model_to_entity(result)

        except OperationalError as e:
            raise ConnectionFailure() from e
        except SQLAlchemyError as e:
            raise TransactionFailure() from e

    @override
    def create(self, entity: UserEntity) -> UserEntity:
        try:
            # map the entity to user model
            user_model = map_entity_to_user_model(entity)
            # add user to the session
            self.session.add(user_model)
            # commit the session
            self.session.commit()
            # return the user entity
            return map_user_model_to_entity(user_model)

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
            raise RepositoryException() from e

    @override
    def update(self, id: int, entity: UserEntity) -> UserEntity:
        try:

            # Get user by id
            user = self.session.query(UserModel).filter(UserModel.id == id).first()
           
            # raise exception if user is not found
            if user is None:
                raise UserNotFound(entity="User", key="id")

            # Map user entity to user model
            user_model = map_entity_to_user_model(entity)
                 
            # Commit session
            self.session.commit()
          
            # Map user model to user entity and return
            return map_user_model_to_entity(user_model)
            
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
            raise RepositoryException() from e

    @override
    def delete(self, id: int) -> bool:
        try:         
            
            # Get user by id
            user = self.session.query(UserModel).filter(UserModel.id == id).first()

            # raise exception if user is not found
            if user is None:
                raise UserNotFound(entity="User", key="id")

            # Delete user model
            self.session.delete(user)
            
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
