from app.persistence.memory_repository import MemoryRepository
from app.models import City

class CityService:
    @staticmethod
    def get_all_cities():
        return MemoryRepository.get_all(City)

    @staticmethod
    def get_city_by_id(city_id):
        return MemoryRepository.get(City, city_id)
