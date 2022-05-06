from flask import Flask
# importe sua instância da Blueprint
from app.routes.product_route import bp

def init_app(app: Flask):
    # registre sua blueprint no app
    app.register_blueprint(bp)
