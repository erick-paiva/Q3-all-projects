# Desenvolva sua classe Music abaixo
from sqlalchemy import Column, Integer, String, ForeignKey, Time
from app.configs.database import db

class Music(db.Model):
    
    __tablename__ = "musics"
    
    music_id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    duration = Column(Time, nullable=False)
    
    album_id = Column(Integer, ForeignKey("albums.album_id"))
    
