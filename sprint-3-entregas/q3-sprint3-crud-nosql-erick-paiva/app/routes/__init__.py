from flask import Flask
from app.routes.home_route import home_routes


def init_app(app: Flask):
    home_routes(app)