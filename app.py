from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from database import app, db
from resources.user import UserRegister, UserLogin
from resources.item import ItemList

api = Api(app)
app.config['JWT_SECRET_KEY'] = "your-secret-key"
jwt = JWTManager(app)

api.add_resource(UserRegister, '/register')
api.add_resource(UserLogin, '/login')
api.add_resource(ItemList, '/items')

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
