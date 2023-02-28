from sqlalchemy import Column, Integer, String, Boolean, JSON, ForeignKey
from src.models.base import Base


class Product(Base):
    __tablename__ = "goods"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    code = Column(String(length=15), unique=True, nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)
    manufacture_id = Column(Integer, ForeignKey('manufactures.id'), nullable=False)
    description = Column(JSON)
    is_available = Column(Boolean, nullable=False)
