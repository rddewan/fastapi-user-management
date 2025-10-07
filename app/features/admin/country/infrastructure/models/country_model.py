

from sqlalchemy import Column, DateTime, Integer, String
from app.core.data.source.local.base import Base
from sqlalchemy.sql import func

class CountryModel(Base):
    __tablename__ = "countries"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    country_code = Column(String, unique=True, nullable=False)
    currency_code = Column(String, nullable=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now(), nullable=True)