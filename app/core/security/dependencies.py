

from app.core.security.bcrypt_password_service import BcryptPasswordService
from app.core.security.ipassword_service import IPasswordService


def get_password_service() -> IPasswordService:
    return BcryptPasswordService()