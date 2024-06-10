from abc import ABC, abstractmethod
from typing import List, Union
from uuid import UUID
from datetime import datetime
from ..models.city import City
from ..models.amenity import Amenities
from ..models.review import Review
from ..models.country import Country
from ..models.place import Place
from ..models.user import User

class IPersistenceManager(ABC):
    @abstractmethod
    def save(self, entity: Union[Place, User, City, Amenities, Review, Country]):
        pass

    @abstractmethod
    def get(self, entity_id: UUID, entity_type: type) -> Union[Place, User, City, Amenities, Review, Country]:
        pass

    @abstractmethod
    def update(self, entity: Union[Place, User, City, Amenities, Review, Country]):
        pass

    @abstractmethod
    def delete(self, entity_id: UUID, entity_type: type):
        pass

class DataManager(IPersistenceManager):
    def __init__(self):
        pass

    def save(self, entity: Union[Place, User, City, Amenities, Review, Country]):
        if isinstance(entity, Place):
            self.save_place(entity)
        elif isinstance(entity, User):
            self.save_user(entity)
        elif isinstance(entity, City):
            self.save_city(entity)
        elif isinstance(entity, Amenities):
            self.save_amenities(entity)
        elif isinstance(entity, Review):
            self.save_review(entity)
        elif isinstance(entity, Country):
            self.save_country(entity)
        else:
            raise TypeError("Type d'entité non pris en charge")

    def get(self, entity_id: UUID, entity_type: type) -> Union[Place, User, City, Amenities, Review, Country]:
        if entity_type == Place:
            return self.get_place(entity_id)
        elif entity_type == User:
            return self.get_user(entity_id)
        elif entity_type == City:
            return self.get_city(entity_id)
        elif entity_type == Amenities:
            return self.get_amenities(entity_id)
        elif entity_type == Review:
            return self.get_review(entity_id)
        elif entity_type == Country:
            return self.get_country(entity_id)
        else:
            raise TypeError("Type d'entité non pris en charge")

    def update(self, entity: Union[Place, User, City, Amenities, Review, Country]):
        if isinstance(entity, Place):
            self.update_place(entity)
        elif isinstance(entity, User):
            self.update_user(entity)
        elif isinstance(entity, City):
            self.update_city(entity)
        elif isinstance(entity, Amenities):
            self.update_amenities(entity)
        elif isinstance(entity, Review):
            self.update_review(entity)
        elif isinstance(entity, Country):
            self.update_country(entity)
        else:
            raise TypeError("Type d'entité non pris en charge")

    def delete(self, entity_id: UUID, entity_type: type):
        if entity_type == Place:
            self.delete_place(entity_id)
        elif entity_type == User:
            self.delete_user(entity_id)
        elif entity_type == City:
            self.delete_city(entity_id)
        elif entity_type == Amenities:
            self.delete_amenities(entity_id)
        elif entity_type == Review:
            self.delete_review(entity_id)
        elif entity_type == Country:
            self.delete_country(entity_id)
        else:
            raise TypeError("Type d'entité non pris en charge")
