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
from src.models.schemas.user_password_change import UserPasswordChangeSchema
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

    def remove(self, removable_user_id: int, main_user_id: int) -> None:
        if not self.validate_user_action(main_user_id=main_user_id, changeable_user_id=removable_user_id):
            self.exceptions.forbidden_error()
        user = self.get_user_by_id(removable_user_id)
        self.session.delete(user)
        self.session.commit()

    def authorize(self, phone: str, password: str) -> Union[JWT, None]:
        user = self.get_user_by_phone(phone)

        if not user:
            return None
        if not self.password_check(input_password=password, user_password=user.get_user_password()):
            return None

        return self.create_token(user_id=user.id)

    def validate_user_action(self, main_user_id: int, changeable_user_id: int) -> bool:
        return self.get_user_by_id(user_id=main_user_id).is_admin or (main_user_id == changeable_user_id)

    def change_user_password(self, main_user_id: int, changeable_user_password: UserPasswordChangeSchema):
        main_user = self.get_user_by_id(main_user_id)
        user = self.get_user_by_id(changeable_user_password.user_id)
        user_old_password: UserPassword = UserPassword(
            user.password,
            user.salt
        )

        user_have_permissions: bool = self.validate_user_action(
            main_user_id=main_user_id,
            changeable_user_id=changeable_user_password.user_id
        )
        if not user_have_permissions:
            self.exceptions.forbidden_error()

        is_password_matches: bool = self.password_check(changeable_user_password.old_password, user_old_password)
        # Если пользователь администратор и изменяется пароль другой учетной записи, то сверка пароля не производится
        if not (is_password_matches or (main_user.is_admin and (main_user_id != changeable_user_password.user_id))):
            self.exceptions.password_error()

        user_new_password = self.password_hash(changeable_user_password.new_password)
        user.password = user_new_password.password
        user.salt = user_new_password.salt

        self.session.commit()

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
    def verify_token(token: str) -> Optional[int]:
        try:
            payload = jwt.decode(token, settings.jwt_secret, algorithms=[settings.jwt_algorithm])
        except JWTError:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Некорректный токен")

        return int(payload.get('sub'))
