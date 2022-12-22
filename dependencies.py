from config_db import SessionLocal
from repositories.album_repository import AlbumRepository
from repositories.singer_repository import SingerRepository
from repositories.track_repository import TrackRepository

def get_singer_repository():
    """Retorna una nueva instancia del repositorio de Singers"""
    return SingerRepository()

def get_album_repository():
    """Retorna una nueva instancia del repositorio de Albums"""
    return AlbumRepository()

def get_track_repository():
    """Retorna una nueva instancia del repositorio de Tracks"""
    return TrackRepository()

def get_db():
    """Función helper para obtener una session de la base de datos"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()