from typing import Optional
from app.core.exceptions.repository import UniqueConstraintFailure
from app.features.shared.user.application.interface.iuser_repository import (
    IUserRepository,
)
from app.features.shared.user.domain.exceptions.exception import UserAlreadyExistException
from app.features.shared.user.domain.user_entity import UserEntity


class UserService:

    def __init__(self, user_respository: IUserRepository):
        self.user_repository = user_respository
        pass

    def get_all_users(
        self, skip: int, limit: int, search: Optional[str] = None
    ) -> tuple[list[UserEntity], int, int]:
        return self.user_repository.get_all(skip=skip, limit=limit, search=search)
    
    def get_user_byt_id(self, id: int) -> UserEntity:
        return self.user_repository.get_by_id(id=id)
    
    def create_user(self, user: UserEntity) -> UserEntity:
        try:
            return self.user_repository.create(entity= user)
        except UniqueConstraintFailure:
            raise UserAlreadyExistException(entity= user, key=user.email)
        
    def update_user(self, id: int, user: UserEntity) -> UserEntity:
        try:
            return self.user_repository.update(id= id, entity= user)
        except UniqueConstraintFailure:
            raise UserAlreadyExistException(entity= user, key=user.email)
        
    def delete_user(self, id: int) -> bool:
        return self.user_repository.delete(id=id)

        
