import hashlib
import os
from datetime import datetime, timedelta
from fastapi import HTTPException
from typing import Optional
from fastapi import Depends
from starlette import status
from src.core.settings import settings
from src.db.db import Session, get_session
from src.models.schemas.jwt import JWT
from src.models.schemas.user_create import UserCreateSchema
from src.models.user_password import UserPassword
from src.models.user import User
from jose import jwt, JWTError


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

    def get_user(self, user_id: int):
        user = (
            self.session
            .query(User)
            .filter(
                User.id == user_id
            )
            .first()
        )
        return user

    def get_user_by_phone(self, user_phone: str):
        user = (
            self.session
            .query(User)
            .filter(
                User.phone == user_phone
            )
            .first()
        )
        return user

    def remove(self, user_id: int):
        user = self.get_user(user_id)
        self.session.delete(user)
        self.session.commit()
        return user

    def authorize(self, phone: str, password: str):
        user = self.get_user_by_phone(phone)

        if not user:
            return None
        if not self.password_check(input_password=password, user_password=user.get_user_password()):
            return None

        return self.create_token(user_id=user.id)

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
            input_password.encode(settings.password_encoding),
            user_password.salt,
            100000
        )

        return input_password_hash == user_password.password

    @staticmethod
    def create_token(user_id: int) -> JWT:
        now = datetime.utcnow()
        payload = {
            'iat': now,
            'exp': now + timedelta(seconds=settings.jwt_time_expire_seconds),
            'sub': str(user_id)
        }
        token = jwt.encode(payload, settings.jwt_secret, algorithm=settings.jwt_algorithm)
        return JWT(access_token=token)

    @staticmethod
    def verify_token(token: JWT) -> Optional[int]:
        try:
            payload = jwt.decode(token.access_token, settings.jwt_secret, algorithms=[settings.jwt_algorithm])
        except JWTError:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Некорректный токен")

        return payload.get('sub')
