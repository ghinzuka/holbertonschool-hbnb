from basemodel import BaseModel
from uuid import uuid4
from datetime import datetime

class City(BaseModel):
    _cities = []

    def __init__(self, name: str):
        super().__init__()
        existing_city = self.get_city_by_name(name)
        if existing_city:
            raise ValueError(f"The city '{name}' already exists.")
        else:
            self.city_id = uuid4()
            self.name = name
            self.add_city()

    def add_city(self):
        City._cities.append({
            'city_id': self.city_id,
            'name': self.name,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        })

    @classmethod
    def get_all_cities(cls):
        return cls._cities

    @staticmethod
    def get_city_by_name(name: str):
        for city in City._cities:
            if city['name'] == name:
                return city
        return None