from flask_restx import Namespace, Resource

amenity_ns = Namespace("amenities", description="Operations on amenities")

@amenity_ns.route("/")
class AmenityList(Resource):
    def get(self):
        return {
  "amenities": [
    {
      "id": 1,
      "name": "Wi-Fi",
      "description": "High-speed internet available throughout the property",
      "created_at": "2025-03-23T10:00:00",
      "updated_at": "2025-03-23T10:00:00"
    },
    {
      "id": 2,
      "name": "Air Conditioning",
      "description": "Comfortable, adjustable temperature control",
      "created_at": "2025-03-22T09:30:00",
      "updated_at": "2025-03-22T09:30:00"
    },
    {
      "id": 3,
      "name": "Swimming Pool",
      "description": "Outdoor pool open from 9am to 6pm",
      "created_at": "2025-03-21T12:00:00",
      "updated_at": "2025-03-21T12:00:00"
    }
  ]
}

    def post(self):
        return {"message": "Create a new amenity"}
