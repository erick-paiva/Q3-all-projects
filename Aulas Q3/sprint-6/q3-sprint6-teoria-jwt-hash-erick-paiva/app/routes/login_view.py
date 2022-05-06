from flask import Blueprint, request
from http import HTTPStatus
from app.models.user_model import UserModel


bp_login = Blueprint("bp_login", __name__)


@bp_login.route("/login", methods=["POST"])
def login():
    user_data = request.get_json()

    found_user: UserModel = UserModel.query.filter_by(email=user_data["email"]).first()

    if not found_user:
        return {"message": "User not found"}, HTTPStatus.NOT_FOUND

    if found_user.verify_password(user_data["password"]):
        return {"message": "Sucess Login"}, HTTPStatus.OK
    else:
        return {"message": "Unauthorized"}, HTTPStatus.UNAUTHORIZED

