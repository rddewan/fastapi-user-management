from typing import override
import bcrypt
from app.core.security.ipassword_service import IPasswordService


class BcryptPasswordService(IPasswordService):

    @override
    def hash_password(self, password: str) -> str:
        hashed = bcrypt.hashpw(
            password=password.encode(encoding="utf-8"),
            salt=bcrypt.gensalt(),
        )
        return hashed.decode(encoding="utf-8")

    @override
    def verify_password(seld, plain_password: str, hashed_password: str) -> bool:
        try:
            return bcrypt.checkpw(
                password=plain_password.encode(encoding="utf-8"),
                hashed_password=hashed_password.encode(encoding="utf-8")
            )
        except Exception:
            return False
