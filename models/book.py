from sqlalchemy import Column, Integer, String
from .base import Base

class Book(Base):
    __tablename__ = 'book'
    id = Column(Integer, primary_key=True)
    title = Column(String(length=50))
    subtitleTag = Column(String(length=50))
