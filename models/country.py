from typing import List
from city import City

class Country:
    def __init__(self, name: str, cities: List[City] = None):
        self.name = name
        self.cities = cities or []
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("name must be a string")
        self.__name = value
    
    def add_city(self, city: List[City]):
        if city in self.cities:
            raise ValueError(f"City {city.name} is already added to this country")
        self.cities.append(city)

    def get_all_cities(self):
        return list(City.get_all_cities())