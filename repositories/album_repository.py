from sqlalchemy.orm import Session
from models.album_model import AlbumModel
from typing import List

class AlbumRepository:
    """AlbumRepository: Clase diseñada para el manejo de la persistencia de los Albunes"""

    async def findAlbumsByArtistId(self, artist_id: int, db: Session) -> List[AlbumModel]:
        """Consulta todos los albunes de un artista por ID"""

        album_list: List[AlbumModel] = db.query(AlbumModel).filter(AlbumModel.artist_id==artist_id).all()
        return album_list
