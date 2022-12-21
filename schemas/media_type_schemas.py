from pydantic import BaseModel

# MediaType base model
class MediaTypeBase(BaseModel):
    media_type_id: int
    name: str

# MediaType DB model
class MediaTypeInDB(MediaTypeBase):
    class Config:
        orm_mode = True