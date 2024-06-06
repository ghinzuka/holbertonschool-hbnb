import re
from typing import List
from uuid import UUID, uuid4
from datetime import datetime
from city import City
from amenity import Amenities
from review import Review
from country import Country

class Place:
    def __init__(self, name: str, description: str, address: str, city_name: str,
                 latitude: float, longitude: float, user_id: UUID, creator_id: UUID,
                 n_room: int, n_bathroom: int, price_per_night: float,
                 n_max_people: int, amenities: Amenities, reviews: List[Review],
                 country: 'Country'):
        
        self.place_id = uuid4()
        self.name = name
        self.description = description
        self.address = address
        self.city_name = city_name
        self.latitude = latitude
        self.longitude = longitude
        self.user_id = user_id
        self.creator_id = creator_id 
        self.n_room = n_room
        self.n_bathroom = n_bathroom
        self.price_per_night = price_per_night
        self.n_max_people = n_max_people
        self.amenities = amenities
        self.reviews = reviews
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        

        if not any(city.name == city_name for city in country.cities):
            raise ValueError(f"The city {city_name} is not found in the country {country.name}")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not value:
            raise TypeError("name must be a non-empty string")
        self._name = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        if not isinstance(value, str):
            raise TypeError("description must be a string")
        if not value:
            raise ValueError("description must not be empty")
        if len(value) > 400:
            raise ValueError("description must be under 400 characters")
        self._description = value

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        if not isinstance(value, str) or not value:
            raise TypeError("address must be a non-empty string")
        
        address_pattern = re.compile(
            r'^[A-Za-z0-9\s,]+,\s*[A-Za-z\s]+,\s*[A-Za-z\s]+,\s*[A-Za-z]{2}\s*\d{5}$'
        )
        
        if not address_pattern.match(value):
            raise ValueError("address must follow a valid format")
        
        self._address = value

    @property
    def city_name(self):
        return self._city_name

    @city_name.setter
    def city_name(self, value):
        if not isinstance(value, str) or not value:
            raise TypeError("city_name must be a non-empty string")
        self._city_name = value

    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, value):
        if not isinstance(value, float) or value is None:
            raise TypeError("latitude must be a non-empty float")
        if value < -90 or value > 90:
            raise ValueError("latitude must be between -90 and 90 degrees")
        self._latitude = value

    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, value):
        if not isinstance(value, float) or value is None:
            raise TypeError("longitude must be a non-empty float")
        if value < -180 or value > 180:
            raise ValueError("longitude must be between -180 and 180 degrees")
        self._longitude = value

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        if not isinstance(value, UUID) or value is None:
            raise TypeError("user_id must be a non-empty UUID")
        self._user_id = value

    @property
    def creator_id(self):
        return self._creator_id

    @creator_id.setter
    def creator_id(self, value):
        if not isinstance(value, UUID) or value is None:
            raise TypeError("creator_id must be a non-empty UUID")
        if hasattr(self, '_creator_id') and self._creator_id is not None:
            if self._user_id != value:
                raise PermissionError("creator_id cannot be modified by other users.")
        else:
            self._creator_id = value

    @property
    def n_room(self):
        return self._n_room

    @n_room.setter
    def n_room(self, value):
        if not isinstance(value, int) or value is None:
            raise TypeError("n_room must be a non-empty integer")
        self._n_room = value

    @property
    def n_bathroom(self):
        return self._n_bathroom

    @n_bathroom.setter
    def n_bathroom(self, value):
        if not isinstance(value, int) or value is None:
            raise TypeError("n_bathroom must be a non-empty integer")
        self._n_bathroom = value

    @property
    def price_per_night(self):
        return self._price_per_night

    @price_per_night.setter
    def price_per_night(self, value):
        if not isinstance(value, float) or value is None:
            raise TypeError("price_per_night must be a non-empty float")
        self._price_per_night = value

    @property
    def n_max_people(self):
        return self._n_max_people

    @n_max_people.setter
    def n_max_people(self, value):
        if not isinstance(value, int) or value is None:
            raise TypeError("n_max_people must be a non-empty integer")
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

    def update(self, user_id: UUID, **kwargs):
        if user_id != self.creator_id:
            raise PermissionError("Only the creator can update this place.")
        
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.updated_at = datetime.now()



