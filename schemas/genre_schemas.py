from pydantic import BaseModel

# Genre base model
class GenreBase(BaseModel):
    genre_id: int
    name: str

# Genre DB model
class GenreInDB(GenreBase):
    class Config:
        orm_mode = True