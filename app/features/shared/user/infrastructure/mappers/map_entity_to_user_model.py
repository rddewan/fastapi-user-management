from typing import Optional

from sqlalchemy import inspect
from sqlalchemy.orm import Mapper
from app.features.shared.user.domain.user_entity import UserEntity
from app.features.shared.user.infrastructure.models.user_model import UserModel


def map_entity_to_user_model(
    entity: UserEntity,
    model: Optional[UserModel] = None,
) -> UserModel:

    if model is None:
        return UserModel(
            id=entity.id,
            username=entity.username,
            full_name=entity.full_name,
            email=entity.email,
            phone=entity.phone,
            is_active=entity.is_active,
            created_at=entity.created_at,
            updated_at=entity.updated_at,
        )
    else:
        mapper: Mapper[UserModel] = inspect(UserModel)
        # extract the column name
        column_names = [cols.key for cols in mapper.column_attrs]

        # primary key
        primary_keys = [cols.key for cols in mapper.primary_key]

        skip = primary_keys + ["created_at", "updated_at"]

        for name in column_names:
            if name in skip:
                continue
            if hasattr(entity, name):
                value = getattr(entity, name)
                if value is not None:
                    setattr(model, name, value)
        return model
