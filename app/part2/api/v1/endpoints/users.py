from flask_restx import Namespace, Resource, fields
from flask import request
from app.business_logic.facade import HBnBFacade

ns = Namespace("users", description="User operations")
facade = HBnBFacade()

user_model = ns.model("User", {
    "id": fields.Integer(readonly=True),
    "name": fields.String(required=True, description="User name"),
    "email": fields.String(required=True, description="User email"),
})

@ns.route("/")
class UserList(Resource):
    @ns.marshal_list_with(user_model)
    def get(self):
        """List all users"""
        return facade.get_all_users()

    @ns.expect(user_model)
    @ns.marshal_with(user_model, code=201)
    def post(self):
        """Create a new user"""
        data = request.json
        return facade.create_user(data), 201
