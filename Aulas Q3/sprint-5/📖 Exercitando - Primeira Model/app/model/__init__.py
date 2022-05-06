from sqlalchemy import Column, Integer, String, Time
from app import db


class Music(db.Model):
    __tablename__ = "musics"

    music_id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    duration = Column(Time, nullable=False)