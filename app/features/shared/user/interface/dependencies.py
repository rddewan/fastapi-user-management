from sqlalchemy.orm import Session
from typing import Annotated
from fastapi import Depends

from app.core.providers.db import get_db_session
from app.core.security.dependencies import get_password_service
from app.core.security.ipassword_service import IPasswordService
from app.features.shared.user.application.interface.iuser_repository import IUserRepository
from app.features.shared.user.application.user_service import UserService
from app.features.shared.user.infrastructure.repository.user_repository import UserRepository


def get_user_repository(
    db_session: Annotated[Session, Depends(get_db_session)]) -> IUserRepository:
    return UserRepository(db_session)

def get_user_service(
    user_repository: Annotated[IUserRepository, Depends(get_user_repository)],
    password_service: Annotated[IPasswordService, Depends(get_password_service)]
    ) -> UserService:
    return UserService(user_repository, password_service)