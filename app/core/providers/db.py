
from typing import Generator
from sqlalchemy.orm import Session
from app.core.providers.env_config import get_env_config
from app.core.data.source.local.database import Database

def get_db_session() -> Generator[Session, None, None]:
    """
    Get database session

    Returns:
        Generator[Session, None, None]: Database session
    """
    session = Database(get_env_config()).get_session()
    return session