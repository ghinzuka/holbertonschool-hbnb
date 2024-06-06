from uuid import uuid4
from datetime import datetime


class Amenities:
    _amenities = {}

    def __init__(self, name: str):
        if name in Amenities._amenities:
            raise ValueError(f"Amenity '{name}' already exists")
        self.name = name
        self.amenity_id = uuid4()
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        Amenities._amenities[name] = self

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("name must be a string")
        self.__name = value

    @classmethod
    def get_all_amenities(cls):
        return cls._amenities.values()

    @staticmethod
    def get_amenity_by_name(name: str):
        return Amenities._amenities.get(name)
