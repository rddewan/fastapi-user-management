
from typing import Annotated, Optional
from fastapi import Depends, Query, status
from app.core.router.router import get_versioned_router
from app.features.shared.user.application.user_service import UserService
from app.features.shared.user.interface.dependencies import get_user_service
from app.features.shared.user.interface.mappers.map_create_user_schema_to_entity import mapCreateUserSchemaToEntity
from app.features.shared.user.interface.mappers.map_update_user_schema_to_entity import mapUpdateUserEntityToEntity
from app.features.shared.user.interface.schemas import CreateUserRequest, PaginationMeta, UpdateUserRequest, UserListResponse, UserResponse


v1_router = get_versioned_router("v1")

@v1_router.get("/users", status_code=status.HTTP_200_OK)
def get_users(
    user_service: Annotated[UserService, Depends(get_user_service)],
    skip: Annotated[
        int, Query(ge=1, description="Page number should be greater than or equal to 1")
    ],
    limit: Annotated[
        int, Query(ge=1, description="Limit should be greater than or equal to 1")
    ],
    search: Annotated[
        Optional[str], Query(description="Search query for the users")
    ] = None,
) -> UserListResponse:
    result,total, total_page = user_service.get_all_users(skip=skip -1, limit=limit, search=search)
    
    meta: PaginationMeta = PaginationMeta(
        total=total, total_page=total_page, page_size=limit, current_page=skip
    )
    return UserListResponse(
        status="success",
        data=result,
        meta=meta
    )
    
    
@v1_router.get("/users/{user_id}", status_code=status.HTTP_200_OK)
def get_user_by_id(
    user_service: Annotated[UserService, Depends(get_user_service)],
    user_id: int,
) -> UserResponse:
    result = user_service.get_user_by_id(id=user_id)
    

    return UserResponse(
        status="success",
        data=result
    )
    
@v1_router.post("/users", status_code=status.HTTP_201_CREATED)
def create_user(
    user_service: Annotated[UserService, Depends(get_user_service)],
    data: CreateUserRequest,
) -> UserResponse:
    # map the request body to user entity
    user_entity = mapCreateUserSchemaToEntity(user_schems=data)
    
    result = user_service.create_user(user=user_entity)
    

    return UserResponse(
        status="success",
        data=result
    )
    
@v1_router.patch("/users/{user_id}", status_code=status.HTTP_200_OK)
def patch_user(
    user_service: Annotated[UserService, Depends(get_user_service)],
    user_id: int,
    data: UpdateUserRequest,
) -> UserResponse:
    # map the request body to user entity
    user_entity = mapUpdateUserEntityToEntity(user_schema=data)
    
    result = user_service.update_user(id=user_id, user=user_entity)
    

    return UserResponse(
        status="success",
        data=result
    )
    
@v1_router.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(
    user_service: Annotated[UserService, Depends(get_user_service)],
    user_id: int,
) -> None:
    
    user_service.delete_user(id=user_id)
  