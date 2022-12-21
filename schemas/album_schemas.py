from pydantic import BaseModel

# Album base model
class AlbumBase(BaseModel):
    album_id: int
    title: str

# Album DB model
class AlbumInDB(AlbumBase):
    artist_id: int
    class Config:
        orm_mode = True