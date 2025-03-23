from flask_restx import Api

# Initialize the Flask-RESTX API
api = Api()

# You can import other parts of the API here if needed
from .v1 import api as v1_api

# Register the v1 API with the main API
api.add_namespace(v1_api)
