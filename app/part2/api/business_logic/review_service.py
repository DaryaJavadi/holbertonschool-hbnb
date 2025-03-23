from app.persistence.memory_repository import MemoryRepository
from app.models import Review

class ReviewService:
    @staticmethod
    def get_all_reviews():
        return MemoryRepository.get_all(Review)

    @staticmethod
    def get_review_by_id(review_id):
        return MemoryRepository.get(Review, review_id)
