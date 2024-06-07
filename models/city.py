import uuid
from datetime import datetime
from typing import List


class City:
    _cities = {}
    
    def __init__(self, name: str, city_id=None, created_at=None, updated_at=None):
        existing_city = City.get_city_by_name(name)
        if existing_city:
            self.city_id = existing_city.city_id
            self.name = existing_city.name
            self.created_at = existing_city.created_at
            self.updated_at = datetime.now()
        else:
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
    
    @staticmethod
    def get_city_by_name(name: str):
        return City._cities.get(name)
