from app.configs.database import db
from sqlalchemy import Column, Integer, ForeignKey

bands_genres = db.Table(
    "bands_genres",
    Column("band_id", Integer, ForeignKey("bands.band_id")),
    Column("genre_id", Integer, ForeignKey("genres.genre_id")),
)
