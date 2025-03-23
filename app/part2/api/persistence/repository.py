from abc import ABC, abstractmethod

class Repository(ABC):
    @abstractmethod
    def get(self, model, id):
        pass

    @abstractmethod
    def get_all(self, model):
        pass
