import uuid
from datetime import datetime

class City:
    _cities = []

    def __init__(self, name: str):
        existing_city = self.get_city_by_name(name)
        if existing_city:
            raise ValueError(f"The city '{name}' already exists.")
        else:
            self.city_id = uuid.uuid4()
            self.name = name
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            self.add_city()

    def add_city(self):
        City._cities.append({
            'city_id': self.city_id,
            'name': self.name,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        })

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        if not isinstance(value, str) or not value:
            raise TypeError("name must be a non-empty string")
        self._name = value

    @property
    def created_at(self):
        return self._created_at

    @created_at.setter
    def created_at(self, value):
        if not isinstance(value, datetime):
            raise TypeError("created_at must be a datetime instance")
        self._created_at = value

    @property
    def updated_at(self):
        return self._updated_at

    @updated_at.setter
    def updated_at(self, value):
        if not isinstance(value, datetime):
            raise TypeError("updated_at must be a datetime instance")
        self._updated_at = value

    @classmethod
    def get_all_cities(cls):
        return cls._cities

    @staticmethod
    def get_city_by_name(name: str):
        for city in City._cities:
            if city['name'] == name:
                return city
        return None

    def update(self, **kwargs):
        for key, value in kwargs.items():
            if key in ['name']:
                setattr(self, key, value)
        self.updated_at = datetime.now()
        for city in City._cities:
            if city['city_id'] == self.city_id:
                city['name'] = self.name
                city['updated_at'] = self.updated_at
                break

**