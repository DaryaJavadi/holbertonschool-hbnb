from flask import Flask
from app.part2.api.v1 import api as api_blueprint
from app.part2.api.business_logic import user_service, place_service, review_service, amenity_service, city_service, country_service
from app.part2.api.persistence.memory_repository import MemoryRepository  # Ensure the file exists at app/persistence/memory_repository.py

# Initialize the Flask app
app = Flask(__name__)
from flask import Blueprint

# Create a Blueprint instance
api_bp = Blueprint('api_v1', __name__)

# Define routes here
@api_bp.route('/status', methods=['GET'])
def status():
    return {"status": "OK"}

# Register the API blueprint
app.register_blueprint(api_blueprint, url_prefix='/api/v1')

# Set up a repository (use in-memory storage for now)
repository = MemoryRepository()

# Create your business logic classes
user_service = user_service.UserService(repository)
place_service = place_service.PlaceService(repository)
review_service = review_service.ReviewService(repository)
amenity_service = amenity_service.AmenityService(repository)
city_service = city_service.CityService(repository)
country_service = country_service.CountryService(repository)

# Add more initialization as needed
def create_app():
    app = Flask(__name__)
    app.register_blueprint(api_bp, url_prefix='/api/v1')
    return app
