from flask import request
from app.models.user_model import UserModel
from app.configs.database import db

def create_user():
    
    user_data = request.get_json()
    
    password_to_hash = user_data.pop("password")
    
    new_user = UserModel(**user_data)

    new_user.password = password_to_hash
    
    db.session.add(new_user)

    db.session.commit()
    
    return {"message": "User created successfully!"}, 201

def login_user():
    user_data = request.get_json()
    
    found_user: UserModel = (
        UserModel.query.filter_by(email=user_data["email"]).first()
    )
    
    if not found_user:
        return {"message": "User not found!"}, 404
    
    if found_user.verify_password(user_data["password"]):
        return {"message": "User logged in successfully!"}, 200
    else:
        return {"message": "Unauthorized!"}, 401
    