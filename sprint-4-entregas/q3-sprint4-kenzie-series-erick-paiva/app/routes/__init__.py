from flask import Flask, Blueprint
from .series import bp_series

def init_app(app: Flask):
    app.register_blueprint(bp_series)
    