from sqlalchemy import Column, Integer, String, Boolean
from src.models.base import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    second_name = Column(String)
    phone = Column(String)
    email = Column(String)
    is_admin = Column(Boolean)
