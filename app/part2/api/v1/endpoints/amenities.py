from flask_restx import Resource, fields, Namespace
from app.part2.api.business_logic.amenity_service import AmenityService

api = Namespace('amenities', description='Amenity operations')

amenity_model = api.model('Amenity', {
    'id': fields.String(required=True, description='Amenity ID'),
    'name': fields.String(required=True, description='Amenity Name'),
})

class AmenityList(Resource):
    def get(self):
        amenities = AmenityService.get_all_amenities()
        return [amenity.to_dict() for amenity in amenities]

class Amenity(Resource):
    def get(self, amenity_id):
        amenity = AmenityService.get_amenity_by_id(amenity_id)
        if amenity:
            return amenity.to_dict()
        api.abort(404, "Amenity not found")
