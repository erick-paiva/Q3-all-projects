# Desenvolva sua classe Band abaixo
from sqlalchemy import Column, Integer, String
from app.configs.database import db
from sqlalchemy.orm import relationship


class Band(db.Model):
    __tablename__ = "bands"

    band_id = Column(Integer, primary_key=True)
    name = Column(String)

    albums = relationship("Album", back_populates="band")

    genres = relationship("Genre", secondary="bands_genres")
