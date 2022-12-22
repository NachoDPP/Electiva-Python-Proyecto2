from typing import List
from sqlalchemy.orm import Session
from models.artist_model import ArtistModel

from schemas.artist_schemas import ArtistInDB

class SingerRepository:
    """SingerRepository: Clase diseñada para el manejo de la persistencia de los Artistas"""
    
    async def find(self, db: Session) -> List[ArtistInDB]:
        """Consulta todos los artistas en la DB"""
        
        singer_list: List[ArtistInDB] = db.query(ArtistModel).all()
        return singer_list