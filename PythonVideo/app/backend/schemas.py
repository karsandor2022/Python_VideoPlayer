from pydantic import BaseModel

class VideoBase(BaseModel):
    title: str
    url: str

class VideoCreate(VideoBase):
    pass

class Video(VideoBase):
    id: int

    class Config:
        orm_mode = True
