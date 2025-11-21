
from app.features.shared.user.domain.user_entity import UserEntity
from app.features.shared.user.infrastructure.models.user_model import UserModel


def map_user_model_to_entity(model: UserModel) -> UserEntity:
    return UserEntity(
        id=model.id,
        username=model.username,
        full_name=model.full_name,
        email=model.email,
        phone=model.phone,
        is_active=model.is_active,
        created_at=model.created_at,
        updated_at=model.updated_at,
    )