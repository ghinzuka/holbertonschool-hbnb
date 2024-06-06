from uuid import UUID, uuid4
from datetime import datetime


class Amenities:
    __amenities = {}

    def __init__(self, name: str):
        if name in Amenities.__amenities:
            raise ValueError(f"Amenity '{name}' already exists")
        self.name = name
        self.amenity_id = uuid4()
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        Amenities.__amenities[name] = self

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
        return cls.__amenities.values()
