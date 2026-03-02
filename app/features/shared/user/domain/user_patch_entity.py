

from dataclasses import dataclass
from typing import Optional

@dataclass
class UserPatchEntity :
    email: Optional[str] = None
    password: Optional[str] = None
    full_name: Optional[str] = None
    phone: Optional[str] = None 
    is_active: Optional[bool] = None
