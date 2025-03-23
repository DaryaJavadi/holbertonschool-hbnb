from app.persistence.memory_repository import MemoryRepository
from app.models import User

class UserService:
    @staticmethod
    def get_all_users():
        return MemoryRepository.get_all(User)

    @staticmethod
    def get_user_by_id(user_id):
        return MemoryRepository.get(User, user_id)
