from .base import BaseModel

class Place(BaseModel):
    def __init__(self, name: str, description: str, address: str, city_name: str,
                 latitude: float, longitude: float, n_room: int, n_bathroom: int,
                 price_per_night: float, n_max_people: int, amenities: str, reviews: str):
        super().__init__()
        self.name = name
        self.description = description
        self.address = address
        self.city_name = city_name
        self.latitude = latitude
        self.longitude = longitude
        self.n_room = n_room
        self.n_bathroom = n_bathroom
        self.price_per_night = price_per_night
        self.n_max_people = n_max_people
        self.amenities = amenities
        self.reviews = reviews
        
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
        if len(value) > 1000:
            raise ValueError("description must be under 1000 characters")
        self._description = value

    @property
    def address(self):
        return self._address
    
    @address.setter
    def address(self, value):
        if not isinstance(value, str) or not value:
            raise TypeError("address must be a non-empty string")
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
        if not isinstance(value, float):
            raise TypeError("latitude must be a non-empty float")
        if value < -90 or value > 90:
            raise ValueError("latitude must be between -90 and 90 degrees")
        self._latitude = value

    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, value):
        if not isinstance(value, float):
            raise TypeError("longitude must be a non-empty float")
        if value < -180 or value > 180:
            raise ValueError("longitude must be between -180 and 180 degrees")
        self._longitude = value

    @property
    def n_room(self):
        return self._n_room

    @n_room.setter
    def n_room(self, value):
        if not isinstance(value, int):
            raise TypeError("n_room must be a non-empty integer")
        if value < 0:
            raise ValueError("number of rooms need to be greater than 0")
        self._n_room = value

    @property
    def n_bathroom(self):
        return self._n_bathroom

    @n_bathroom.setter
    def n_bathroom(self, value):
        if not isinstance(value, int):
            raise TypeError("n_bathroom must be a non-empty integer")
        if value < 0:
            raise ValueError("number of bathrooms need to be greater than 0")
        self._n_bathroom = value

    @property
    def price_per_night(self):
        return self._price_per_night

    @price_per_night.setter
    def price_per_night(self, value):
        if not isinstance(value, float):
            raise TypeError("price_per_night must be a non-empty float")
        if value < 0:
            raise ValueError("price need to be greater than 0")
        self._price_per_night = value

    @property
    def n_max_people(self):
        return self._n_max_people

    @n_max_people.setter
    def n_max_people(self, value):
        if not isinstance(value, int):
            raise TypeError("n_max_people must be a non-empty integer")
        if value < 0:
            raise ValueError("max people need to be greater than 0")
        self._n_max_people = value

    @property
    def reviews(self):
        return self._reviews

    @reviews.setter
    def reviews(self, value):
        if not isinstance(value, str) or not value:
            raise TypeError("reviews must be a non-empty string")
        self._reviews = value
    
    @property
    def amenities(self):
        return self._amenities

    @amenities.setter
    def amenities(self, value):
        if not isinstance(value, str) or not value:
            raise TypeError("amenities must be a non-empty string")
        self._amenities = value

    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "address": self.address,
            "city_name": self.city_name,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "n_room": self.n_room,
            "n_bathroom": self.n_bathroom,
            "price_per_night": self.price_per_night,
            "n_max_people": self.n_max_people,
            "amenities": self.amenities,
            "reviews": self.reviews,
            "id": self.id 
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            name=data["name"],
            description=data["description"],
            address=data["address"],
            city_name=data["city_name"],
            latitude=data["latitude"],
            longitude=data["longitude"],
            n_room=data["n_room"],
            n_bathroom=data["n_bathroom"],
            price_per_night=data["price_per_night"],
            n_max_people=data["n_max_people"],
            amenities=data["amenities"],
            reviews=data["reviews"]
        )
