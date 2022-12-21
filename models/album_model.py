from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from config_db import Base

class AlbumModel(Base):
    __tablename__ = 'albums'

    album_id = Column(Integer, primary_key=True, index=True, name='AlbumId')
    title = Column(String(160), name='Title')
    artist_id = Column(Integer, ForeignKey('artists.ArtistId'), name='ArtistId')

    # ORM Relationships
    artist = relationship('ArtistModel')