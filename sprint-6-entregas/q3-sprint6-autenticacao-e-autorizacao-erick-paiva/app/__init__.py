
from flask import Flask
from app.configs import database, jwt_auth, migration
from app import routes


def create_app():
    app = Flask(__name__)

    database.init_app(app)
    migration.init_app(app)
    jwt_auth.init_app(app)
    routes.init_app(app)

    return app
