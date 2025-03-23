from flask import Flask
from flask_restx import Api
from app.api.v1.endpoints.users import ns as users_ns
from app.api.v1.endpoints.places import ns as places_ns
from app.api.v1.endpoints.reviews import ns as reviews_ns
from app.api.v1.endpoints.amenities import ns as amenities_ns
from app.api.v1.endpoints.cities import ns as cities_ns
from app.api.v1.endpoints.countries import ns as countries_ns

app = Flask(__name__)
api = Api(app, title="HBnB Evolution API", version="1.0", description="API for HBnB")

# Register namespaces
api.add_namespace(users_ns, path="/users")
api.add_namespace(places_ns, path="/places")
api.add_namespace(reviews_ns, path="/reviews")
api.add_namespace(amenities_ns, path="/amenities")
api.add_namespace(cities_ns, path="/cities")
api.add_namespace(countries_ns, path="/countries")

if __name__ == "__main__":
    app.run(debug=True)
