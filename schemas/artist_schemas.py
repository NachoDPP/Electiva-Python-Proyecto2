from pydantic import BaseModel

# Artist base model
class ArtistBase(BaseModel):
    artist_id: int
    name: str

# Artist DB model
class ArtistInDB(ArtistBase):
    class Config:
        orm_mode = True