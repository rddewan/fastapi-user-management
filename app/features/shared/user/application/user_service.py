from typing import Optional
from app.core.exceptions.repository import UniqueConstraintFailure
from app.core.security.ipassword_service import IPasswordService
from app.features.shared.user.application.interface.iuser_repository import (
    IUserRepository,
)
from app.features.shared.user.domain.exceptions.exception import (
    InvalidPasswordException,
    UserAlreadyExistException,
)
from app.features.shared.user.domain.user_entity import UserEntity
from app.features.shared.user.domain.user_patch_entity import UserPatchEntity


class UserService:

    def __init__(
        self,
        user_respository: IUserRepository,
        password_service: IPasswordService,
    ):
        self.user_repository = user_respository
        self.password_service = password_service

    def get_all_users(
        self, skip: int, limit: int, search: Optional[str] = None
    ) -> tuple[list[UserEntity], int, int]:
        return self.user_repository.get_all(skip=skip, limit=limit, search=search)

    def get_user_by_id(self, id: int) -> UserEntity:
        return self.user_repository.get_by_id(id=id)

    def create_user(self, user: UserEntity, password: str) -> UserEntity:
        try:
            user.hashed_password = self.password_service.hash_password(password=password)
            return self.user_repository.create(entity=user)
        except UniqueConstraintFailure:
            raise UserAlreadyExistException(entity=user, key=user.email)

    def update_user(self, id: int, user: UserPatchEntity) -> UserEntity:
        try:
            return self.user_repository.update(id=id, entity=user)
        except UniqueConstraintFailure:
            raise UserAlreadyExistException(entity=user, key=user.email)

    def update_user_email(
        self, id: int, current_password: str, email: str
    ) -> UserEntity:
        # get user from the db
        user = self.user_repository.get_by_id(id=id)
        # gurd
        if not user.hashed_password:
            raise InvalidPasswordException()
        # user hashed password
        hashed_password = user.hashed_password
        # verify the user password
        isValid = self.password_service.verify_password(
            plain_password=current_password, hashed_password=hashed_password
        )
        if not isValid:
            raise InvalidPasswordException()

        entity = UserPatchEntity(email=email)
        return self.user_repository.update(id=id, entity=entity)

    def update_user_password(
        self, id: int, current_password: str, new_password: str
    ) -> UserEntity:
        # get user from the db
        user = self.user_repository.get_by_id(id=id)
        # gurd
        if not user.hashed_password:
            raise InvalidPasswordException()
        
        # user hashed password
        hashed_password = user.hashed_password
        # verify the user password
        isValid = self.password_service.verify_password(
            plain_password=current_password, hashed_password=hashed_password
        )
        if not isValid:
            raise InvalidPasswordException()

        # hash the new password
        new_password_hash = self.password_service.hash_password(password=new_password)

        # create a patch entity for password update
        entity = UserPatchEntity(password=new_password_hash)
        return self.user_repository.update(id=id, entity=entity)

    def delete_user(self, id: int) -> bool:
        return self.user_repository.delete(id=id)
