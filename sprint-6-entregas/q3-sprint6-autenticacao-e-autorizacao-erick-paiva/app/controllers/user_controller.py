from http import HTTPStatus
from flask import current_app, jsonify, request
from app.helpers.user_helper import checkKeys
from app.models.user_model import UserModel
from app.configs.database import db
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity


session = db.session


def commit_changes(new_user):
    session.add(new_user)
    session.commit()


def create_user():
    user_data = request.get_json()

    password_to_hash = user_data.pop("password")

    new_user = UserModel(**user_data)

    new_user.password = password_to_hash
    try:
        commit_changes(new_user)
    except:
        return {"message": "email already exists"}, HTTPStatus.BAD_REQUEST

    return jsonify(new_user), HTTPStatus.CREATED


def signin_user():
    user_data = request.get_json()
    found_user: UserModel = UserModel.query.filter_by(
        email=user_data["email"]).first()

    if not found_user:
        return {"message": "User not found"}, HTTPStatus.NOT_FOUND

    token = create_access_token(found_user)
    if found_user.verify_password(user_data["password"]):
        return jsonify({"access_token": token}), HTTPStatus.OK
    else:
        return {"message": "Incorrect email or password"}, HTTPStatus.UNAUTHORIZED


@jwt_required()
def get_users():

    user = get_jwt_identity()

    return jsonify(user), HTTPStatus.OK


@jwt_required()
def update_user():
    data = request.get_json()
    user_email = get_jwt_identity()["email"]
    user: UserModel = UserModel.query.filter_by(
        email=user_email).first()

    verified_keys = checkKeys(data.keys())
    if verified_keys:
        return verified_keys
    for key, value in data.items():
        setattr(user, key, value)

    try:
        commit_changes(user)
    except:
        return {"message": "Email already in use"}, HTTPStatus.BAD_REQUEST

    return jsonify(user), HTTPStatus.OK


@jwt_required()
def delete_user():
    user_email = get_jwt_identity()
    user = UserModel.query.filter_by(email=user_email["email"]).first()
    current_app.db.session.delete(user)
    current_app.db.session.commit()
    return jsonify({"msg": f"User {user.name} has been deleted."}), HTTPStatus.OK
