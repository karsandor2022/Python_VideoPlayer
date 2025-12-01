from sqlalchemy.orm import Session
from . import models, schemas

def get_videos(db: Session):
    return db.query(models.Video).all()

def create_video(db: Session, video: schemas.VideoCreate):
    db_video = models.Video(title=video.title, url=video.url)
    db.add(db_video)
    db.commit()
    db.refresh(db_video)
    return db_video