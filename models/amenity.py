from uuid import uuid4
from datetime import datetime


class Amenities:
    _amenities = []

    def __init__(self, names: list):
        if not all(isinstance(name, str) for name in names):
            raise TypeError("Tous les noms doivent être des chaînes de caractères")
        if any(name in [amenity['name'] for amenity in Amenities._amenities] for name in names):
            raise ValueError("Un ou plusieurs noms existent déjà")
        
        self.names = names
        self.amenity_ids = [uuid4() for _ in names]
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        
        for name, amenity_id in zip(self.names, self.amenity_ids):
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
        if not all(isinstance(name, str) for name in value):
            raise TypeError("Tous les noms doivent être des chaînes de caractères")
        self.__names = value

    @classmethod
    def get_all_amenities(cls):
        return cls._amenities

    @staticmethod
    def get_amenities_by_name(name: str):
        return [amenity for amenity in Amenities._amenities if amenity['name'] == name]
