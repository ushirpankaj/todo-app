from app import app, db
from flask import jsonify, request
from models.User import User
from werkzeug.security import generate_password_hash

@app.route("/register", methods=['POST'])
def register():
    data = request.get_json()
    
    data['password'] =  generate_password_hash(data["password"])

    user = User(**data)
    db.session.add(user)
    db.session.commit()
    return {"message": "User Created", "id": user.id}, 201


