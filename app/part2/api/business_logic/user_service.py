from app.part2.api.persistence.memory_repository import MemoryRepository
from app.part2.api.models import User

class UserService:
    @staticmethod
    def get_all_users():
        return MemoryRepository.get_all(User)

    @staticmethod
    def get_user_by_id(user_id):
        return MemoryRepository.get(User, user_id)
