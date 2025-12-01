from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .database import SessionLocal
from . import crud, schemas

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[schemas.Video])
def list_videos(db: Session = Depends(get_db)):
    return crud.get_videos(db)

@router.post("/", response_model=schemas.Video)
def add_video(video: schemas.VideoCreate, db: Session = Depends(get_db)):
    return crud.create_video(db, video)