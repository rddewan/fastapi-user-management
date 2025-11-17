

from abc import ABC, abstractmethod

from app.features.shared.user.domain.user_entity import UserEntity


class IUserRepository(ABC):
    """
    Interface from user repository
    """

    @abstractmethod
    def get_all(self, skip: int, limit: int) -> list[UserEntity]:
        pass
    
    @abstractmethod
    def get_by_id(self, id: int) -> UserEntity:
        pass

    @abstractmethod
    def create(self, entity: UserEntity) -> UserEntity:
        pass
    
    @abstractmethod
    def update(self, id: int, entity: UserEntity) -> UserEntity:
        pass
    
    @abstractmethod
    def delete(self, id: int) -> bool:
        pass
        