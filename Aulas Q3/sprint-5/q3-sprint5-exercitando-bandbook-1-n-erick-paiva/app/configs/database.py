from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()


def init_app(app: Flask):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DB_URI")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    app.db = db

    # Declarar as models para serem reconhecidas pelo SQLALCHEMY
    from app.models.album_model import Album
    from app.models.band_model import Band
    from app.models.music_model import Music