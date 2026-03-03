

from abc import ABC, abstractmethod


class IPasswordService(ABC):
    
    @abstractmethod
    def hash_password(self, password:str) -> str:
        pass
    
    @abstractmethod
    def verify_password(seld, plain_password: str, hashed_password: str)-> bool:
        pass
    