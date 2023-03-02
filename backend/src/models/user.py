from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.dialects.postgresql import BYTEA
from src.models.user_password import UserPassword
from src.models.base import Base


class User(Base):
    def __init__(self, user_password: UserPassword, first_name: str, second_name: str, phone: str, email: str):
        self.password = user_password.password
        self.salt = user_password.salt
        self.first_name = first_name
        self.second_name = second_name
        self.phone = phone
        self.email = email

    def get_user_password(self):
        return UserPassword(password=self.password, salt=self.salt)

    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    second_name = Column(String, nullable=False)
    phone = Column(String, unique=True)
    email = Column(String, unique=True)
    is_admin = Column(Boolean, default=False, nullable=False)
    password = Column(BYTEA, nullable=False)
    salt = Column(BYTEA, nullable=False)
