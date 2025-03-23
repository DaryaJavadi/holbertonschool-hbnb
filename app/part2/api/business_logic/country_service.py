from app.persistence.memory_repository import MemoryRepository
from app.models import Country

class CountryService:
    @staticmethod
    def get_all_countries():
        return MemoryRepository.get_all(Country)

    @staticmethod
    def get_country_by_id(country_id):
        return MemoryRepository.get(Country, country_id)
