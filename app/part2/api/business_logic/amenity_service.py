from app.part2.api.persistence.memory_repository import MemoryRepository
from app.part2.api.models import Amenity

class AmenityService:
    @staticmethod
    def get_all_amenities():
        return MemoryRepository.get_all(Amenity)

    @staticmethod
    def get_amenity_by_id(amenity_id):
        return MemoryRepository.get(Amenity, amenity_id)
