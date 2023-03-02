from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from src.models.base import Base


class Picture(Base):
    __tablename__ = "pictures"
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('goods.id'), nullable=False)
    product = relationship('Product', back_populates="pictures")
    url = Column(String, nullable=False)
