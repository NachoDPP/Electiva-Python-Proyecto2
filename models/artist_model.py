from sqlalchemy import Column, Integer, String 

from config_db import Base

class ArtistModel(Base):
    __tablename__ = 'artists'

    artist_id = Column(Integer, primary_key=True, index=True, name='ArtistId')
    name = Column(String(120), name='Name')