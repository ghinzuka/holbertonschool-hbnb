from uuid import UUID, uuid4
from datetime import datetime
from place import Place
from basemodel import BaseModel

class Review(BaseModel):
    _reviews = []

    def __init__(self, user_id: UUID, place_id: UUID, text: str, rating: int, places_list=None):
        super().__init__()
        if places_list is None:
            places_list = Place.get_places()
        self.user_id = user_id
        self.place_id = place_id
        self.text = text
        self.rating = rating

        for place in places_list:
            if place['place_id'] == place_id:
                place_creator_id = place['creator_id']
                if user_id == place_creator_id:
                    raise PermissionError("The creator of the place cannot write a review for their own place.")

        self._reviews.append({
            'review_id': self.id,
            'user_id': self.user_id,
            'place_id': self.place_id,
            'text': self.text,
            'rating': self.rating,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        })

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        if not isinstance(value, str) or not value:
            raise TypeError("text must be a non-empty string")
        self._text = value

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, value):
        if not isinstance(value, int) or value is None:
            raise TypeError("rating must be a non-empty integer")
        if value < 1 or value > 5:
            raise ValueError("rating must be between 1 and 5")
        self._rating = value
    
    @classmethod
    def get_reviews_by_user_id(cls, user_id: UUID):
        return [review for review in cls._reviews if review['user_id'] == user_id]