from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from models import User
from database import db
from schemas import UserSchema

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    user_schema = UserSchema()
    errors = user_schema.validate(data)
    
    if errors:
        return jsonify(errors), 400

    email = data['email']
    password = data['password']
    
    if User.query.filter_by(email=email).first():
        return jsonify({"message": "User already exists."}), 400

    hashed_password = generate_password_hash(password)
    new_user = User(email=email, hashed_password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User created successfully."}), 201

@auth_bp.route('/signin', methods=['POST'])
def signin():
    data = request.get_json()
    user_schema = UserSchema(partial=True)
    errors = user_schema.validate(data)
    
    if errors:
        return jsonify(errors), 400

    email = data['email']
    password = data['password']
    
    user = User.query.filter_by(email=email).first()
    if user and check_password_hash(user.hashed_password, password):
        return jsonify({"message": "Login successful."}), 200

    return jsonify({"message": "Invalid email or password."}), 401