from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from src.models.base import Base


class Cart(Base):
    __tablename__ = "cart"
    id = Column(Integer, primary_key=True)
    count = Column(Integer)
    user_id = Column(Integer, ForeignKey('users.id'), index=True)
    user = relationship('User', backref='users')
    product_id = Column(Integer, ForeignKey('goods.id'), index=True)
    product = relationship('Product', backref='goods')
