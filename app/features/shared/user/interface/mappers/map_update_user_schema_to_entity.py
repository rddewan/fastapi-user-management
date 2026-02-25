


from app.features.shared.user.domain.user_patch_entity import UserPatchEntity
from app.features.shared.user.interface.schemas import UpdateUserRequest


def mapUpdateUserEntityToEntity(user_schema: UpdateUserRequest) -> UserPatchEntity:
    return UserPatchEntity(
        full_name=user_schema.full_name,
        phone=user_schema.phone,
        is_active=user_schema.is_active,
    )
    