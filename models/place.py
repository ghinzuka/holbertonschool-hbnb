from typing import List
from uuid import UUID, uuid4
from datetime import datetime
from city import City
from amenity import Amenities
from review import Review

class Place:
    def __init__(self, name: str, description: str, address: str, city_name: str,
                 latitude: float, longitude: float, user_id: UUID, n_room: int,
                 n_bathroom: int, price_per_night: float, n_max_people: int,
                 amenities: Amenities, reviews: List[Review]):
        
        self.place_id = uuid4()
        self.name = name
        self.description = description
        self.address = address
        self.city_name = city_name
        self.latitude = latitude
        self.longitude = longitude
        self.user_id = user_id
        self.n_room = n_room
        self.n_bathroom = n_bathroom
        self.price_per_night = price_per_night
        self.n_max_people = n_max_people
        self.amenities = amenities
        self.reviews = reviews
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        
        # Validate city_name with the country
        if not any(city.name == city_name for city in country.cities):
            raise ValueError(f"The city {city_name} is not found in the country {country.name}")
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("name must be a string")
        self._name = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        if not isinstance(value, str):
            raise TypeError("description must be a string")
        self._description = value

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        if not isinstance(value, str):
            raise TypeError("address must be a string")
        self._address = value

    @property
    def city_name(self):
        return self._city_name

    @city_name.setter
    def city_name(self, value):
        if not isinstance(value, str):
            raise TypeError("city_name must be a string")
        self._city_name = value

    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, value):
        if not isinstance(value, float):
            raise TypeError("latitude must be a float")
        if value < -90 or value > 90:
            raise ValueError("latitude must be between -90 and 90 degrees")
        self._latitude = value

    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, value):
        if not isinstance(value, float):
            raise TypeError("longitude must be a float")
        if value < -180 or value > 180:
            raise ValueError("longitude must be between -180 and 180 degrees")
        self._longitude = value

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        if not isinstance(value, UUID):
            raise TypeError("user_id must be a UUID")
        self._user_id = value

    @property
    def n_room(self):
        return self._n_room

    @n_room.setter
    def n_room(self, value):
        if not isinstance(value, int):
            raise TypeError("n_room must be an integer")
        self._n_room = value

    @property
    def n_bathroom(self):
        return self._n_bathroom

    @n_bathroom.setter
    def n_bathroom(self, value):
        if not isinstance(value, int):
            raise TypeError("n_bathroom must be an integer")
        self._n_bathroom = value

    @property
    def price_per_night(self):
        return self._price_per_night

    @price_per_night.setter
    def price_per_night(self, value):
        if not isinstance(value, float):
            raise TypeError("price_per_night must be a float")
        self._price_per_night = value

    @property
    def n_max_people(self):
        return self._n_max_people

    @n_max_people.setter
    def n_max_people(self, value):
        if not isinstance(value, int):
            raise TypeError("n_max_people must be an integer")
        self._n_max_people = value

    @property
    def amenities(self):
        return self._amenities

    @amenities.setter
    def amenities(self, value):
        if not isinstance(value, Amenities):
            raise TypeError("amenities must be an instance of Amenities")
        self._amenities = value

    @property
    def reviews(self):
        return self._reviews

    @reviews.setter
    def reviews(self, value):
        if not all(isinstance(review, Review) for review in value):
            raise TypeError("all reviews must be instances of Review")
        self._reviews = value

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

    def update(self, **kwargs):
        # Allow updating attributes with key-value pairs
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.updated_at = datetime.now()
