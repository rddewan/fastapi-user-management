


from typing import Optional
from pydantic import BaseModel

from app.features.shared.user.domain.user_entity import UserEntity


class CreateUserRequest(BaseModel):
    username: str
    email: str
    password: str
    password_confirmation: str 
    full_name: Optional[str]
    phone: Optional[str]
    is_active: Optional[str]
    

class UpdateUserRespone(BaseModel):
    full_name: Optional[str]
    phone: Optional[str]
    is_active: Optional[str]
    

class UpdateEmailRequest(BaseModel):
    email: str
    current_password: str
    

class UpdatePasswordRequest(BaseModel):
    current_password: str 
    new_password: str
    new_password_confirmation: str


class PaginationMeta(BaseModel):
    total: int
    total_page: int
    page_size: int
    current_page: int

class UserListResponse(BaseModel):
    status: str
    data: list[UserEntity]
    meta: PaginationMeta
    

class UserResponse(BaseModel):
    status: str
    data: UserEntity