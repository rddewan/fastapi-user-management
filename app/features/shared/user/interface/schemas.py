

import re
from typing import Optional
from pydantic import BaseModel, ConfigDict, EmailStr, Field, field_validator, model_validator


class CreateUserRequest(BaseModel):
    username: str = Field(..., min_length=3, max_length=20)
    email: EmailStr
    password: str = Field(..., min_length=8, max_length=20)
    password_confirmation: str = Field(..., min_length=8, max_length=20)
    full_name: Optional[str] = None
    phone: Optional[str] = None
    is_active: Optional[str] = None
    
    @field_validator("password")
    @classmethod
    def validate_password_streangth(cls, value: str) -> str:
        if not re.search(r"[A-Z]", value):
            raise ValueError("password must contain at least one uppercase letter")
        if not re.search(r"[a-z]", value):
            raise ValueError("password must contain at least one lowercase letter")
        if not re.search(r"[\d]", value):
            raise ValueError("password must contain at least one numner")
        if not re.search(r"[^A-Za-z0-9, value]", value):
            raise ValueError("password must contain at least one special character")
        
        return value
    
    @model_validator(mode="after")
    def validate_passwoed_confirmation(self) -> "CreateUserRequest":
        if self.password != self.password_confirmation:
            raise ValueError("password and password_confirmation do not match")
        return self
    

class UpdateUserRequest(BaseModel):
    full_name: Optional[str] = None
    phone: Optional[str] = None
    is_active: Optional[bool] = None
    

class UpdateEmailRequest(BaseModel):
    email: str
    current_password: str = Field(..., min_length=8, max_length=20)
    
    @field_validator("current_password")
    @classmethod
    def validate_password_streangth(cls, value: str) -> str:
        if not re.search(r"[A-Z]", value):
            raise ValueError("password must contain at least one uppercase letter")
        if not re.search(r"[a-z]", value):
            raise ValueError("password must contain at least one lowercase letter")
        if not re.search(r"[\d]", value):
            raise ValueError("password must contain at least one numner")
        if not re.search(r"[^A-Za-z0-9, value]", value):
            raise ValueError("password must contain at least one special character")
        
        return value
    

class UpdatePasswordRequest(BaseModel):
    current_password: str = Field(..., min_length=8, max_length=20)
    new_password: str = Field(..., min_length=8, max_length=20)
    new_password_confirmation: str = Field(..., min_length=8, max_length=20)
    
    @field_validator("new_password")
    @classmethod
    def validate_password_streangth(cls, value: str) -> str:
        if not re.search(r"[A-Z]", value):
            raise ValueError("password must contain at least one uppercase letter")
        if not re.search(r"[a-z]", value):
            raise ValueError("password must contain at least one lowercase letter")
        if not re.search(r"[\d]", value):
            raise ValueError("password must contain at least one numner")
        if not re.search(r"[^A-Za-z0-9, value]", value):
            raise ValueError("password must contain at least one special character")
        
        return value
    
    @model_validator(mode="after")
    def validate_passwoed_confirmation(self) -> "UpdatePasswordRequest":
        if self.new_password != self.new_password_confirmation:
            raise ValueError("password and password_confirmation do not match")
        return self


class UserData(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    id: Optional[int] = None
    username: str
    email: str
    full_name: Optional[str] = None
    phone: Optional[str] = None
    is_active: bool = True

class PaginationMeta(BaseModel):
    total: int
    total_page: int
    page_size: int
    current_page: int

class UserListResponse(BaseModel):
    status: str
    data: list[UserData]
    meta: PaginationMeta
    

class UserResponse(BaseModel):
    status: str
    data: UserData