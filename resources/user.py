from flask_restful import Resource, reqparse
from models import User
from database import db
from flask_jwt_extended import create_access_token
from flask import jsonify

class UserRegister(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', required=True)
        parser.add_argument('email', required=True)
        parser.add_argument('password', required=True)
        data = parser.parse_args()

        if User.query.filter_by(email=data['email']).first():
            return {"message": "Email already exists"}, 400

        user = User(username=data['username'], email=data['email'])
        user.set_password(data['password'])
        db.session.add(user)
        db.session.commit()

        return {"message": "User created successfully"}, 201

class UserLogin(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('email', required=True)
        parser.add_argument('password', required=True)
        data = parser.parse_args()

        user = User.query.filter_by(email=data['email']).first()
        if user and user.check_password(data['password']):
            token = create_access_token(identity=user.id)
            return {"access_token": token}, 200
        return {"message": "Invalid credentials"}, 401
