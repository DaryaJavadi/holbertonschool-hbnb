from flask_restx import Namespace, Resource

review_ns = Namespace("reviews", description="Operations on reviews")

@review_ns.route("/")
class ReviewList(Resource):
    def get(self):
        return {
  "reviews": [
    {
      "id": 1,
      "user_id": 1,
      "place_id": 5,
      "rating": 4,
      "comment": "Great place, very clean and spacious!",
      "created_at": "2025-03-21T18:30:00",
      "updated_at": "2025-03-21T18:30:00"
    },
    {
      "id": 2,
      "user_id": 2,
      "place_id": 3,
      "rating": 5,
      "comment": "Amazing experience, highly recommend!",
      "created_at": "2025-03-20T15:00:00",
      "updated_at": "2025-03-20T15:00:00"
    }
  ]
}

    def post(self):
        return {"message": "Create a new review"}
