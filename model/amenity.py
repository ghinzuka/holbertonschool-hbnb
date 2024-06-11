from basemodel import BaseModel
from uuid import uuid4
from datetime import datetime

class Amenities(BaseModel):
    _amenities = []

    def __init__(self, names: list):
        super().__init__()
        self.names = names
        self.amenity_ids = []

        for name in self.names:
            existing_amenity = self.get_amenities_by_name(name)
            if existing_amenity:
                self.amenity_ids.append(existing_amenity[0]['amenity_id'])
            else:
                amenity_id = uuid4()
                self.amenity_ids.append(amenity_id)
                Amenities._amenities.append({
                    'name': name,
                    'amenity_id': amenity_id,
                    'created_at': self.created_at,
                    'updated_at': self.updated_at
                })

    @property
    def names(self):
        return self.__names

    @names.setter
    def names(self, value):
        print("Checking names:", value)
        if not all(isinstance(name, str) for name in value):
            raise TypeError("Tous les noms doivent être des chaînes de caractères")
        self.__names = list(set(value))

    @classmethod
    def get_all_amenities(cls):
        return cls._amenities

    @staticmethod
    def get_amenities_by_name(name: str):
        return [amenity for amenity in Amenities._amenities if amenity['name'] == name]