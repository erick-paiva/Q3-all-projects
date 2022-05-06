from flask import Blueprint, current_app, request, jsonify
from http import HTTPStatus
from app.models.user_model import UserModel


bp_user = Blueprint("bp_user", __name__)


@bp_user.route("/user", methods=["POST"])
def create_user():
    session = current_app.db.session
    user_data = request.get_json()

    password_to_hash = user_data.pop("password")
    
    new_user = UserModel(**user_data)

    new_user.password = password_to_hash

    session.add(new_user)
    session.commit()

    return jsonify(new_user), HTTPStatus.CREATED