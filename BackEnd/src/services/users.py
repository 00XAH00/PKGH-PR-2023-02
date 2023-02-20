import hashlib
import os
from fastapi import Depends

from src.core.settings import settings
from src.db.db import Session, get_session
from src.models.UserPassword import UserPassword


class UserService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    @staticmethod
    def password_hash(password: str) -> UserPassword:
        salt = os.urandom(32)
        password_hash = hashlib.pbkdf2_hmac(
            settings.password_hash_algorithm,
            password.encode(settings.password_encoding),
            salt,
            100000
        )
        return UserPassword(password=password_hash, salt=salt)

    @staticmethod
    def password_check(input_password: str, user_password: UserPassword) -> bool:
        input_password_hash = hashlib.pbkdf2_hmac(
            settings.password_hash_algorithm,
            input_password.encode(settings.password_encoding),  # Конвертирование пароля в байты
            user_password.salt,
            100000
        )

        return input_password_hash == user_password.password
