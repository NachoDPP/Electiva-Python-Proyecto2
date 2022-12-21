from sqlalchemy import Column, Integer, String 

from config_db import Base

class GenreModel(Base):
    __tablename__ = 'genres'

    genre_id = Column(Integer, primary_key=True, index=True, name='GenreId')
    name = Column(String(120), name='Name')