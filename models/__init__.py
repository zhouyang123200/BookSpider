from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config.settings import DATABASE
from .base import Base
from .book import Book

engine = create_engine(DATABASE.get('NAME'))
Session = sessionmaker()
Session.configure(bind=engine)
Base.metadata.create_all(engine)