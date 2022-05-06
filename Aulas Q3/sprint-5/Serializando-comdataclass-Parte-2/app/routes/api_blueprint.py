from flask import Blueprint
from app.routes.cachorro_blueprint import bp_dogs
from app.routes.dono_blueprint import bp_dono


bp_api = Blueprint("api", __name__)

bp_api.register_blueprint(bp_dogs)
bp_api.register_blueprint(bp_dono)
