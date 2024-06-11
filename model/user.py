from uuid import UUID, uuid4
from datetime import datetime
from review import Review
from place import Place
from basemodel import BaseModel
from review import Review
from place import Place

class User(BaseModel):
    _registered_emails = set()
    _users_data = []

    def __init__(self, email: str, password: str, first_name: str, last_name: str):
        super().__init__()
        if email in User._registered_emails:
            raise ValueError(f"Email {email} is already taken.")
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.place_names = []  # Placeholder for place names
        self.reviews = []  

        User._registered_emails.add(email)
        
        # Add user data to the list of dictionaries
        User._users_data.append({
            'user_id': self.id,
            'email': self.email,
            'password': self.password,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'place_names': self.place_names,
            'reviews': self.reviews,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        })

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if not isinstance(value, str) or not value:
            raise TypeError("email must be a non-empty string")
        self._email = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        if not isinstance(value, str) or not value:
            raise TypeError("password must be a non-empty string")
        self._password = value

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str) or not value:
            raise TypeError("first_name must be a non-empty string")
        self._first_name = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        if not isinstance(value, str) or not value:
            raise TypeError("last_name must be a non-empty string")
        self._last_name = value

    def load_places_names(self):
        self.place_names = []
        for place_data in Place.get_places():
            if place_data['user_id'] == self.id:
                place_name = place_data['name']
                self.place_names.append(place_name)

    def load_reviews(self):
        self.reviews = []
        for review_data in Review.get_reviews():
            if review_data['user_id'] == self.id:
                review = Review(**review_data)
                self.reviews.append(review)

    @classmethod
    def find_user_by_email(cls, email):
        for user_data in cls._users_data:
            if user_data['email'] == email:
                return cls(**user_data)
        return None

    @classmethod
    def find_user_by_id(cls, user_id):
        for user_data in cls._users_data:
            if user_data['user_id'] == user_id:
                return cls(**user_data)
        return None 