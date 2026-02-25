

from dataclasses import dataclass
from typing import Optional

@dataclass
class UserPatchEntity :
    full_name: Optional[str] = None
    phone: Optional[str] = None 
    is_active: Optional[bool] = None
