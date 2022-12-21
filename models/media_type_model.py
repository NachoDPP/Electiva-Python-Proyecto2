from sqlalchemy import Column, Integer, String 

from config_db import Base

class MediaTypeModel(Base):
    __tablename__ = 'media_types'

    media_type_id = Column(Integer, primary_key=True, index=True, name='MediaTypeId')
    name = Column(String(120), name='Name')