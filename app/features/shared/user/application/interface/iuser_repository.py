

from abc import ABC, abstractmethod
from typing import Optional

from app.features.shared.user.domain.user_entity import UserEntity
from app.features.shared.user.domain.user_patch_entity import UserPatchEntity


class IUserRepository(ABC):
    """
    Interface from user repository
    """

    @abstractmethod
    def get_all(self, skip: int, limit: int, search: Optional[str] = None) -> tuple[list[UserEntity], int, int]:
        pass
    
    @abstractmethod
    def get_by_id(self, id: int) -> UserEntity:
        pass

    @abstractmethod
    def create(self, entity: UserEntity) -> UserEntity:
        pass
    
    @abstractmethod
    def update(self, id: int, entity: UserPatchEntity) -> UserEntity:
        pass
    
    @abstractmethod
    def delete(self, id: int) -> bool:
        pass
        