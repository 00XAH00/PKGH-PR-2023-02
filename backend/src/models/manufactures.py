from sqlalchemy import Column, Integer, String
from src.models.base import Base


class Manufacture(Base):
    __tablename__ = "manufactures"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
