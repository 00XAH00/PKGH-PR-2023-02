from sqlalchemy import Column, Integer, String
from src.models.base import Base


class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
