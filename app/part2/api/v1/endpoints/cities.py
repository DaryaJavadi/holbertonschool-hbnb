from flask_restx import Resource, fields, Namespace
from app.part2.api.business_logic.city_service import CityService

api = Namespace('cities', description='City operations')

city_model = api.model('City', {
    'id': fields.String(required=True, description='City ID'),
    'name': fields.String(required=True, description='City Name'),
})

class CityList(Resource):
    def get(self):
        cities = CityService.get_all_cities()
        return [city.to_dict() for city in cities]

class City(Resource):
    def get(self, city_id):
        city = CityService.get_city_by_id(city_id)
        if city:
            return city.to_dict()
        api.abort(404, "City not found")
