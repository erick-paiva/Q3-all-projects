from flask import Flask
from flask_migrate import Migrate


def init_app(app: Flask):

    from app.models.vaccine_model import Vacina

    Migrate(app, app.db)
