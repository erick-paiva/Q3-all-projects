# Desenvolva sua classe Album abaixo


from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from app.configs.database import db

class Album(db.Model):
    __tablename__ = "albums"
    
    
    album_id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    release_date = Column(DateTime, nullable=False)
    
    band_id = Column(Integer, ForeignKey("bands.band_id"))
    band = relationship("Band", back_populates="albums")
    musics = relationship("Music", backref="album")
    