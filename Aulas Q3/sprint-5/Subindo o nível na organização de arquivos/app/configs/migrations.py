from flask import Flask
from flask_migrate import Migrate

def init_app(app: Flask):
    migrate = Migrate(app, app.db)


