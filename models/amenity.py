from uuid import uuid4
from datetime import datetime


class Amenities:
<<<<<<< HEAD
    _amenities = {}

    def __init__(self, name: str):
        if name in Amenities._amenities:
            raise ValueError(f"Amenity '{name}' already exists")
        self.name = name
        self.amenity_id = uuid4()
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        Amenities._amenities[name] = self

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("name must be a string")
        self.__name = value

    @classmethod
    def get_all_amenities(cls):
        return cls._amenities.values()

    @staticmethod
    def get_amenity_by_name(name: str):
        return Amenities._amenities.get(name)
=======
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
>>>>>>> Baptiste
