from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.dialects.postgresql import BYTEA
from src.models.UserPassword import UserPassword
from src.models.base import Base


class User(Base):
    def __init__(self, user_password: UserPassword):
        self.password = user_password.password
        self.salt = user_password.salt

    def get_user_password(self):
        return UserPassword(password=self.password, salt=self.salt)

    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    second_name = Column(String)
    phone = Column(String)
    email = Column(String)
    is_admin = Column(Boolean)
    password = Column(BYTEA)
    salt = Column(BYTEA)
