from typing import List
class Country:
    def __init__(self, name: str, cities: List[City] = []):
        self.name = name
        self.cities = []
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("name must be a string")
        self.__name = value
