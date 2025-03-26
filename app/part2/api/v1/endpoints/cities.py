from flask_restx import Namespace, Resource

city_ns = Namespace("cities", description="Operations on cities")

@city_ns.route("/")
class CityList(Resource):
    def get(self):
        return {
  "cities": [
    {
      "id": 1,
      "name": "San Francisco",
      "state": "California",
      "country_id": 1,
      "population": 883305,
      "created_at": "2025-03-23T08:00:00",
      "updated_at": "2025-03-23T08:00:00"
    },
    {
      "id": 2,
      "name": "Paris",
      "state": "Île-de-France",
      "country_id": 2,
      "population": 2148327,
      "created_at": "2025-03-22T10:00:00",
      "updated_at": "2025-03-22T10:00:00"
    }
  ]
}

    def post(self):
        return {"message": "Create a new city"}
