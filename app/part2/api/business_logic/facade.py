from app.part2.api.business_logic.user_service import UserService
from app.part2.api.business_logic.review_service import ReviewService
from app.part2.api.business_logic.amenity_service import AmenityService
from app.part2.api.business_logic.city_service import CityService
from app.part2.api.business_logic.country_service import CountryService
from app.part2.api.persistence.memory_repository import MemoryRepository

class Facade:
    def __init__(self):
        # Initialize all services with the repository
        self.user_service = UserService(MemoryRepository())
        self.review_service = ReviewService(MemoryRepository())
        self.amenity_service = AmenityService(MemoryRepository())
        self.city_service = CityService(MemoryRepository())
        self.country_service = CountryService(MemoryRepository())

    # User operations
    def create_user(self, user_data):
        return self.user_service.create_user(user_data)

    def get_user(self, user_id):
        return self.user_service.get_user(user_id)

    def update_user(self, user_id, user_data):
        return self.user_service.update_user(user_id, user_data)

    def delete_user(self, user_id):
        return self.user_service.delete_user(user_id)

    # Review operations
    def create_review(self, review_data):
        return self.review_service.create_review(review_data)

    def get_review(self, review_id):
        return self.review_service.get_review(review_id)

    def update_review(self, review_id, review_data):
        return self.review_service.update_review(review_id, review_data)

    def delete_review(self, review_id):
        return self.review_service.delete_review(review_id)

    # Amenity operations
    def create_amenity(self, amenity_data):
        return self.amenity_service.create_amenity(amenity_data)

    def get_amenity(self, amenity_id):
        return self.amenity_service.get_amenity(amenity_id)

    def update_amenity(self, amenity_id, amenity_data):
        return self.amenity_service.update_amenity(amenity_id, amenity_data)

    def delete_amenity(self, amenity_id):
        return self.amenity_service.delete_amenity(amenity_id)

    # City operations
    def create_city(self, city_data):
        return self.city_service.create_city(city_data)

    def get_city(self, city_id):
        return self.city_service.get_city(city_id)

    def update_city(self, city_id, city_data):
        return self.city_service.update_city(city_id, city_data)

    def delete_city(self, city_id):
        return self.city_service.delete_city(city_id)

    # Country operations
    def create_country(self, country_data):
        return self.country_service.create_country(country_data)

    def get_country(self, country_id):
        return self.country_service.get_country(country_id)

    def update_country(self, country_id, country_data):
        return self.country_service.update_country(country_id, country_data)

    def delete_country(self, country_id):
        return self.country_service.delete_country(country_id)
