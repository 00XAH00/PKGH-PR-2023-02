from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.models.base import Base


class Review(Base):
    __tablename__ = "reviews"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    body = Column(String)
    stars_count = Column(Integer)
    user_id = Column(Integer, ForeignKey('users.id'), index=True)
    user = relationship('User', backref='users')
    product_id = Column(Integer, ForeignKey('goods.id'), index=True)
    product = relationship('Product', backref='goods')
