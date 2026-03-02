from typing import Optional
from app.core.exceptions.repository import UniqueConstraintFailure
from app.features.shared.user.application.interface.iuser_repository import (
    IUserRepository,
)
from app.features.shared.user.domain.exceptions.exception import UserAlreadyExistException
from app.features.shared.user.domain.user_entity import UserEntity
from app.features.shared.user.domain.user_patch_entity import UserPatchEntity


class UserService:

    def __init__(self, user_respository: IUserRepository):
        self.user_repository = user_respository
        pass

    def get_all_users(
        self, skip: int, limit: int, search: Optional[str] = None
    ) -> tuple[list[UserEntity], int, int]:
        return self.user_repository.get_all(skip=skip, limit=limit, search=search)
    
    def get_user_by_id(self, id: int) -> UserEntity:
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
        
    def update_user_email(self, id: int, current_password: str, email: str) -> UserEntity:
        try:
            # TODO: validate the password (current_password with password stored in the DB)
            
            entity = UserPatchEntity(email=email)
            return self.user_repository.update(id= id, entity= entity)
        except UniqueConstraintFailure:
            raise UserAlreadyExistException(entity= "User", key=email)
        
    def update_user_password(self, id: int, current_password: str, new_password: str) -> UserEntity:
        try:
            # TODO: validate the password (current_password with password stored in the DB)
            
            # create a patch entity for password update
            entity = UserPatchEntity(password=new_password)
            return self.user_repository.update(id= id, entity= entity)
        except UniqueConstraintFailure:
            raise UserAlreadyExistException(entity="User", key=id)
        
    def delete_user(self, id: int) -> bool:
        return self.user_repository.delete(id=id)

        
