from flask import request
from app.part2.api.models import db, User
from flask_restx import Namespace, Resource

user_ns = Namespace("users", description="User operations")

@user_ns.route('/')
class UserList(Resource):
    def get(self):
        # Fetch all users
        users = User.query.all()
        user_list = [{"id": user.id, "username": user.username, "email": user.email, 
                      "first_name": user.first_name, "last_name": user.last_name, 
                      "is_admin": user.is_admin} for user in users]
        return {"users": user_list}

    def post(self):
        try:
            # Get the request JSON data
            data = request.get_json()

            # Debugging: Log the incoming data
            print(f"Received data: {data}")

            # Ensure required fields are in the request
            if not data or not data.get('username') or not data.get('email') or not data.get('password') or not data.get('first_name') or not data.get('last_name'):
                return {"message": "Missing required fields"}, 400

            # Create a new user instance, including is_admin if it's provided
            new_user = User(
                username=data['username'],
                email=data['email'],
                first_name=data['first_name'],
                last_name=data['last_name'],
                password=data['password'],
                is_admin=data.get('is_admin', False)  # Default to False if not provided
            )

            # Debugging: Log the new user object
            print(f"New user: {new_user}")

            # Add the new user to the database
            db.session.add(new_user)
            db.session.commit()

            # Prepare the user data dictionary to return as JSON response
            user_data = {
                "id": new_user.id,
                "username": new_user.username,
                "email": new_user.email,
                "first_name": new_user.first_name,
                "last_name": new_user.last_name,
                "is_admin": new_user.is_admin
            }

            # Return the newly created user in JSON format
            return user_data, 201

        except Exception as e:
            # Log the error and return a 500 error
            print(f"Error creating user: {e}")
            return {"message": "Internal Server Error"}, 500