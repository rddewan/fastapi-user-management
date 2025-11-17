

from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class UserEntity:
    username: str
    email: str
    hashed_password: str
    is_active: bool = True
    id: Optional[int] = None
    full_name: Optional[str] = None
    phone: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    