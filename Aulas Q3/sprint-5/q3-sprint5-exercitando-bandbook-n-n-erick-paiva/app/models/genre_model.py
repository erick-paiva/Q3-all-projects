from sqlalchemy import Column, Integer, String
from app.configs.database import db


class Genre(db.Model):
    __tablename__ = "genres"

    genre_id = Column(Integer, primary_key=True)
    name = Column(String)
