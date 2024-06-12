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

    def to_dict(self):
        country_dict = {
            "name": self.name,
            "city": self.city.to_dict()
        }
        country_dict.update(super().to_dict())  # Ajouter les attributs de BaseModel
        return country_dict

    @classmethod
    def from_dict(cls, data):
        instance = cls(
            name=data["name"],
            city=City.from_dict(data["city"]) 
        )
        base_instance = BaseModel.from_dict(data)
        instance.id = base_instance.id
        instance.created_at = base_instance.created_at
        instance.updated_at = base_instance.updated_at
        return instance