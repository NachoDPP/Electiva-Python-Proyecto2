from sqlalchemy.orm import Session
from models.album_model import AlbumModel
from models.track_model import TrackModel
from typing import List

from schemas.track_schemas import TrackInDB

class TrackRepository:
    """TrackRepository: Clase diseñada para el manejo de la persistencia de las canciones"""

    async def findTracksByAlbumId(self, album_id: int, db: Session) -> List[TrackInDB]:
        """Consulta todas las canciones de un album por ID de un artista"""

        track_list: List[TrackInDB] = db.query(TrackModel).filter(TrackModel.album_id==album_id).all()
        return track_list


    async def findTrackByArtistId(self, artist_id: int, db: Session) -> List[TrackInDB]:
        """Consulta todas las canciones de un artista por ID"""

        track_list: List[TrackInDB] = db.query(TrackModel).join(AlbumModel, AlbumModel.album_id==TrackModel.album_id).filter(AlbumModel.artist_id==artist_id).all()
        return track_list


    async def findOneById(self, track_id: int, db: Session) -> TrackInDB:
        """Consulta el detalle de una canción por ID"""

        track: TrackInDB = db.query(TrackModel).get(track_id)
        return track

