import re
from typing import List
from uuid import UUID, uuid4
from datetime import datetime
from place import Place
from review import Review

class User:
    def __init__(self, email: str, password: str, first_name: str, last_name: str):
        self.user_id = uuid4()
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.places = []
        self.reviews = []
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def add_place(self, place: Place):
        place.added_by_user_id = self.user_id
        self.places.append(place)

    def remove_place(self, place: Place):
        if place in self.places:
            self.places.remove(place)

    def add_review(self, review: Review):
        self.reviews.append(review)

    def remove_review(self, review: Review):
        if review in self.reviews:
            self.reviews.remove(review)

    def update(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.updated_at = datetime.now()

    def get_reviews_ids(self):
        reviews_ids = []
        for review in self.reviews:
            if review.user_id == self.user_id:
                reviews_ids.append(review.review_id)
        return reviews_ids 