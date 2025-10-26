from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class CountryEntity:
    name: str
    country_code: str
    currency_code: str
    id: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
