from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required
from models import Item
from database import db

class ItemList(Resource):
    @jwt_required()
    def get(self):
        items = Item.query.all()
        return [{"id": item.id, "name": item.name, "description": item.description} for item in items], 200

    @jwt_required()
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', required=True)
        parser.add_argument('description', required=False)
        data = parser.parse_args()

        item = Item(name=data['name'], description=data.get('description'))
        db.session.add(item)
        db.session.commit()

        return {"message": "Item created successfully", "item": {"id": item.id, "name": item.name}}, 201
