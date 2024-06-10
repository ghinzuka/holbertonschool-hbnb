from uuid import UUID, uuid4
from datetime import datetime
from place import Place
from review import Review

class User:
    _registered_emails = set()
    _users_data = []

    def __init__(self, email: str, password: str, first_name: str, last_name: str):
        if email in User._registered_emails:
            raise ValueError(f"Email {email} is already taken.")
        self.user_id = uuid4()
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.places = []
        self.reviews = []
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        User._registered_emails.add(email)
        
        # Add user data to the list of dictionaries
        User._users_data.append({
            'user_id': self.user_id,
            'email': self.email,
            'password': self.password,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'places': self.places,
            'reviews': self.reviews,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        })

    def add_place(self, place: Place):
        place.added_by_user_id = self.user_id
        self.places.append(place)

    def remove_place(self, place: Place):
        if place in self.places:
            self.places.remove(place)

    def update(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                if key == "email":
                    if value in User._registered_emails:
                        raise ValueError(f"Email {value} is already taken.")
                    # Update the email set
                    User._registered_emails.remove(self.email)
                    User._registered_emails.add(value)
                setattr(self, key, value)
        self.updated_at = datetime.now()

    def get_reviews_ids(self):
        reviews_ids = []
        for review in self.reviews:
            if review.user_id == self.user_id:
                reviews_ids.append(review.review_id)
        return reviews_ids 

    @classmethod
    def remove_user(cls, user):
        if user.email in cls._registered_emails:
            cls._registered_emails.remove(user.email)
            # Remove user data from the list
            cls._users_data = [data for data in cls._users_data if data['email'] != user.email]

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