from pydantic import BaseModel

from schemas.album_schemas import AlbumInDB
from schemas.genre_schemas import GenreInDB
from schemas.media_type_schemas import MediaTypeInDB

# Track base model
class TrackBase(BaseModel):
    track_id: int
    name: str
    composer: str | None
    milliseconds: int
    bytes: int
    unit_price: float

# Track DB model
class TrackInDB(TrackBase):
    album: AlbumInDB
    genre: GenreInDB
    media_type: MediaTypeInDB
    class Config:
        orm_mode = True