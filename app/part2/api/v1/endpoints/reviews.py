from flask_restx import Resource, fields, Namespace
from app.part2.api.business_logic.review_service import ReviewService

api = Namespace('reviews', description='Review operations')

review_model = api.model('Review', {
    'id': fields.String(required=True, description='Review ID'),
    'text': fields.String(required=True, description='Review Text'),
})

class ReviewList(Resource):
    def get(self):
        reviews = ReviewService.get_all_reviews()
        return [review.to_dict() for review in reviews]

class Review(Resource):
    def get(self, review_id):
        review = ReviewService.get_review_by_id(review_id)
        if review:
            return review.to_dict()
        api.abort(404, "Review not found")
