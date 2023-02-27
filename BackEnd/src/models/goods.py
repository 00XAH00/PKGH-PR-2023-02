from sqlalchemy import Column, Integer, String, Boolean, JSON
from src.models.base import Base


class Product(Base):
    __tablename__ = "goods"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    price = Column(Integer)
    code = Column(String(length=15))
    description = Column(JSON)
    is_available = Column(Boolean)
