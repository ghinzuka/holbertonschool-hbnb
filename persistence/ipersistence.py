from abc import ABC, abstractmethod

class IPersistenceManager(ABC):
    @abstractmethod
    def create(self, entity):
        pass

    @abstractmethod
    def read(self, entity_id):
        pass

    @abstractmethod
    def update(self, entity_id, data):
        pass

    @abstractmethod
    def delete(self, entity_id):
        pass
