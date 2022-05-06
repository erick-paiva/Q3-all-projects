from flask import Blueprint, Flask
from app.controllers import user_controller

bp = Blueprint("user", __name__)

bp.post("/user")(user_controller.create_user)
bp.post("/login")(user_controller.login_user)
