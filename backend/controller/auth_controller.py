from app import app, db
from flask import jsonify, request
from models.User import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token

@app.route("/register", methods=['POST'])
def register():
    data = request.get_json()
    
    data['password'] =  generate_password_hash(data["password"])

    user = User(**data)
    db.session.add(user)
    db.session.commit()
    return {"message": "User Created", "id": user.id}, 201

@app.route("/login", methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data["username"]).first()

    
    if not user and not check_password_hash(user.password, data["password"]):
        return jsonify({"error":"Invalid credentials"}),401
    
    access_token = create_access_token(
        identity=user.id,
        additional_claims={
        "username": user.username,
        "email": user.email,
        "first_name" : user.first_name,
        "last_name" : user.last_name,
        "phone_number" : user.phone_number
        }
    )
    return {
        "jwt_access_token":access_token,
        "message" : "Login Successful"
    }
        