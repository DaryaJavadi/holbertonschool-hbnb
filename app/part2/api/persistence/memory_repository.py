from app.part2.api.models import User, Place, Review, Amenity, City, Country
from app.part2.api.persistence.repository import Repository
import uuid

class MemoryRepository(Repository):
    # A dictionary to simulate an in-memory storage for different models
    _data = {
        User: {},
        Place: {},
        Review: {},
        Amenity: {},
        City: {},
        Country: {},
    }

    @staticmethod
    def get(model, id):
        return MemoryRepository._data[model].get(id)

    @staticmethod
    def get_all(model):
        return list(MemoryRepository._data[model].values())

    @staticmethod
    def save(model, obj):
        if obj.id is None:
            obj.id = str(uuid.uuid4())  # Generate a new UUID if no ID exists
        MemoryRepository._data[model][obj.id] = obj
        return obj

    @staticmethod
    def delete(model, id):
        if id in MemoryRepository._data[model]:
            del MemoryRepository._data[model][id]
            return True
        return False
