import hashlib
import os
from datetime import datetime, timedelta
from fastapi import HTTPException
from typing import Optional, Union
from fastapi import Depends
from starlette import status
from src.core.settings import settings
from src.db.db import Session, get_session
from src.models.schemas.jwt import JWT
from src.models.schemas.user_create import UserCreateSchema
from src.models.user_password import UserPassword
from src.models.user import User
from jose import jwt, JWTError

from src.services.exception import ExceptionService


class UserService:
    def __init__(self, session: Session = Depends(get_session), exception_service: ExceptionService = Depends()):
        self.session = session
        self.exceptions = exception_service

    def create_user(self, user_create: UserCreateSchema) -> User:
        password = self.password_hash(user_create.password)
        if self.user_having(email=user_create.email, phone=user_create.phone):
            self.exceptions.already_exist("user")
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

    def get_user_by_id(self, user_id: int) -> Union[User, None]:
        user = (
            self.session
            .query(User)
            .filter(
                User.id == user_id
            )
            .first()
        )
        return user

    def get_user_by_phone(self, user_phone: str) -> Union[User, None]:
        user = (
            self.session
            .query(User)
            .filter(
                User.phone == user_phone
            )
            .first()
        )
        return user

    def get_user_by_email(self, email: str) -> Union[User, None]:
        user = (
            self.session.query(User)
            .filter(User.email == email)
            .first()
        )
        return user

    def user_having(self, email: str, phone: str) -> bool:
        return bool(self.get_user_by_email(email) or self.get_user_by_phone(phone))

    def remove(self, user_id: int) -> None:
        user = self.get_user_by_id(user_id)
        self.session.delete(user)
        self.session.commit()

    def authorize(self, phone: str, password: str) -> Union[JWT, None]:
        user = self.get_user_by_phone(phone)

        if not user:
            return None
        if not self.password_check(input_password=password, user_password=user.get_user_password()):
            return None

        return self.create_token(user_id=user.id)

    def validate_user_action(self, main_user_id, changeable_user_id) -> bool:
        return self.get_user_by_id(user_id=main_user_id).is_admin or (main_user_id == changeable_user_id)

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
