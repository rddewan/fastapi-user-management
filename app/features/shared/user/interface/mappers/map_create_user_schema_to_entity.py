

from app.features.shared.user.domain.user_entity import UserEntity
from app.features.shared.user.interface.schemas import CreateUserRequest


def mapCreateUserSchemaToEntity(user_schems: CreateUserRequest) -> UserEntity :
    return UserEntity(
        username=user_schems.username,
        email=user_schems.email,
        full_name=user_schems.full_name,
        phone=user_schems.phone,
        is_active=user_schems.is_active if user_schems.is_active is not None else True
    )
    