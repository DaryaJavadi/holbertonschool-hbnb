from flask_restx import Resource, fields, Namespace
from app.part2.api.business_logic.country_service import CountryService

api = Namespace('countries', description='Country operations')

country_model = api.model('Country', {
    'id': fields.String(required=True, description='Country ID'),
    'name': fields.String(required=True, description='Country Name'),
})

class CountryList(Resource):
    def get(self):
        countries = CountryService.get_all_countries()
        return [country.to_dict() for country in countries]

class Country(Resource):
    def get(self, country_id):
        country = CountryService.get_country_by_id(country_id)
        if country:
            return country.to_dict()
        api.abort(404, "Country not found")
