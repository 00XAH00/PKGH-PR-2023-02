import hashlib
import os
from fastapi import Depends
from src.core.settings import settings
from src.db.db import Session, get_session
from src.models.schemas.user_create import UserCreateSchema
from src.models.user_password import UserPassword
from src.models.user import User


class UserService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def create_user(self, user_create: UserCreateSchema) -> User:
        password = self.password_hash(user_create.password)
        user = User(
            user_password=password,
            first_name=user_create.first_name,
            second_name=user_create.second_name,
            phone=user_create.phone,
            email=user_create.email
        )

        self.session.add(user)
        self.session.commit()

        return user

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
