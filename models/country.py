from base import BaseModel

class Country(BaseModel):
    def __init__(self, city, name: str):
        super().__init__()
        self.name = name
        self.city = city

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("name must be a string")
        self.__name = value
