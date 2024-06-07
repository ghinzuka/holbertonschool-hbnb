from uuid import uuid4
from datetime import datetime


class Amenities:
    _amenities = []

    def __init__(self, names: list):
        print(names)  # Ajout de print pour vérifier les noms fournis
        if not all(isinstance(name, str) for name in names):
            raise TypeError("Tous les noms doivent être des chaînes de caractères")
        if len(names) != len(set(names)):
            raise ValueError("Les noms doivent être uniques dans la liste fournie")
        existing_names = [amenity['name'] for amenity in Amenities._amenities]
        if any(name in existing_names for name in names):
            raise ValueError("Un ou plusieurs noms existent déjà parmi les aménités existants")
        
        self.names = names
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        
        for name in self.names:
            existing_amenity = next((amenity for amenity in Amenities._amenities if amenity['name'] == name), None)
            if existing_amenity:
                self.amenity_id = existing_amenity['amenity_id']
            else:
                self.amenity_id = uuid4()
                Amenities._amenities.append({
                    'name': name,
                    'amenity_id': self.amenity_id,
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
