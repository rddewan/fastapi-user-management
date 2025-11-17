

from abc import ABC, abstractmethod
from typing import Any


class IUserRepository(ABC):
    """
    Interface from user repository
    """

    @abstractmethod
    def get_all(self, skip: int, limit: int) -> list[Any]:
        pass
    
    @abstractmethod
    def get_by_id(self, user_id: int) -> Any:
        pass

    @abstractmethod
    def create(self) -> Any:
        pass
    
    @abstractmethod
    def update(self) -> Any:
        pass
    
    @abstractmethod
    def delete(self) -> bool:
        pass
        