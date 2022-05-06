from flask_jwt_extended import JWTManager
import os


def init_app(app):
    app.config['JWT_SECRET_KEY'] = os.getenv('SECRET_KEY')
    JWTManager(app)