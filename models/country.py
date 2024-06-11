from .base import BaseModel
from .city import City

class Country(BaseModel):
    def __init__(self, city: City, name: str):
        super().__init__()
        self.name = name
        self.city = city

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not value:
            raise TypeError("name must be a non-empty string")
        self.__name = value
    
    @property
    def city(self):
        return self.__city
    
    @city.setter
    def city(self, value):
        if not isinstance(value, City):
            raise TypeError("city must be a City instance")
        self.__city = value
