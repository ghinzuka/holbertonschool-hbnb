import uuid
from datetime import datetime
from typing import List


class City:
    _cities = {}
    
    def __init__(self, name: str, city_id=None, created_at=None, updated_at=None):
        if name in City._cities:
            raise ValueError(f"City {name} already exists")	
        self.name = name
        self.city_id = uuid.uuid4()
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        City._cities[name] = self
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("name must be a string")
        self.__name = value
    
    @classmethod
    def get_all_cities(cls):
        return cls._cities.values()