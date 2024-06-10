from uuid import UUID, uuid4
from datetime import datetime
from place import Place

class Review:
    _reviews = []

    def __init__(self, user_id: UUID, place_id: UUID, text: str, rating: int, places_list=None):
        if places_list is None:
            places_list = Place.get_places()
        self.review_id = uuid4()
        self.user_id = user_id
        self.place_id = place_id
        self.text = text
        self.rating = rating
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        for place in places_list:
            if place['place_id'] == place_id:
                place_creator_id = place['creator_id']
                if user_id == place_creator_id:
                    raise PermissionError("The creator of the place cannot write a review for their own place.")

        Review._reviews.append({
            'review_id': self.review_id,
            'user_id': self.user_id,
            'place_id': self.place_id,
            'text': self.text,
            'rating': self.rating,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        })

    @classmethod
    def get_reviews(cls):
        return cls._reviews

    @staticmethod
    def get_reviews_by_place_id(place_id: UUID):
        return [review for review in Review._reviews if review['place_id'] == place_id]

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
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.updated_at = datetime.now()

    @classmethod
    def delete_review(cls, review_id: UUID):
        cls._reviews = [review for review in cls._reviews if review['review_id'] != review_id]

