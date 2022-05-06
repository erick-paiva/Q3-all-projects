from flask import Flask
from .stock_routes import bp_stock

def init_app(app: Flask):
    app.register_blueprint(bp_stock)
