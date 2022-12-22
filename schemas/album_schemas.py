from pydantic import BaseModel

from schemas.artist_schemas import ArtistInDB

# Album base model
class AlbumBase(BaseModel):
    album_id: int
    title: str

# Album DB model
class AlbumInDB(AlbumBase):
    artist_id: int
    artist: ArtistInDB
    class Config:
        orm_mode = True