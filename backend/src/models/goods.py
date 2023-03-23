from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from src.models.base import Base


class Product(Base):
    __tablename__ = "goods"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    code = Column(String(length=15), unique=True, nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)
    category = relationship('Category', backref='categories')
    manufacture_id = Column(Integer, ForeignKey('manufactures.id'), nullable=False)
    manufacture = relationship('Manufacture', backref='manufactures')
    is_available = Column(Boolean, nullable=False)
    description = Column(String, nullable=False)
    pictures = relationship("Picture", back_populates="product")
