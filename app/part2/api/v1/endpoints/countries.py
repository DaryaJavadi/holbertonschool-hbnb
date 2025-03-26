from flask_restx import Namespace, Resource

country_ns = Namespace("countries", description="Operations on countries")

@country_ns.route("/")
class CountryList(Resource):
    def get(self):
        return {
  "countries": [
    {
      "id": 1,
      "name": "United States",
      "code": "US",
      "created_at": "2025-03-23T08:00:00",
      "updated_at": "2025-03-23T08:00:00"
    },
    {
      "id": 2,
      "name": "France",
      "code": "FR",
      "created_at": "2025-03-22T09:00:00",
      "updated_at": "2025-03-22T09:00:00"
    }
  ]
}

    def post(self):
        return {"message": "Create a new country"}
