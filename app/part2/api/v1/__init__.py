from flask_restx import Api
from flask import Blueprint

from app.part2.api.v1.endpoints.users import user_ns
from app.part2.api.v1.endpoints.reviews import review_ns
from app.part2.api.v1.endpoints.amenities import amenity_ns
from app.part2.api.v1.endpoints.cities import city_ns
from app.part2.api.v1.endpoints.countries import country_ns

api_bp = Blueprint("api", __name__)
api = Api(api_bp, title="HBnB API", version="1.0", description="API for HBnB")

api.add_namespace(user_ns, path="/users")
api.add_namespace(amenity_ns, path="/amenities")
api.add_namespace(city_ns, path="/cities")
api.add_namespace(country_ns, path="/countries")
api.add_namespace(review_ns, path="/reviews")
