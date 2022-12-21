from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from config_db import Base

class TrackModel(Base):
    __tablename__ = 'tracks'

    track_id = Column(Integer, primary_key=True, index=True, name='TrackId')
    name = Column(String(200), name='Name')
    album_id = Column(Integer, ForeignKey('albums.AlbumId'), name='AlbumId')
    media_type_id = Column(Integer, ForeignKey('media_types.MediaTypeId'), name='MediaTypeId')
    genre_id = Column(Integer, ForeignKey('genres.GenreId'), name='GenreId') 
    composer = Column(String(220), name='Composer')
    milliseconds = Column(Integer, name='Milliseconds')
    bytes = Column(Integer, name='Bytes')
    unit_price = Column(Float(10,2), name='UnitPrice')
    
    # ORM Relationship
    album = relationship("Albums")
    genre = relationship("Genres")
    media_type = relationship("MediaTypes")