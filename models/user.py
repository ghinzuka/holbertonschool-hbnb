from uuid import UUID, uuid4
from datetime import datetime
from review import Review
from place import Place

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
        self.place_names = []  # Placeholder for place names
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
            'place_names': self.place_names,
            'reviews': self.reviews,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        })

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

    def load_places_names(self):
        self.place_names = []
        for place_data in Place.get_places():
            if place_data['user_id'] == self.user_id:
                place_name = place_data['name']
                self.place_names.append(place_name)

    def load_reviews(self):
        self.reviews = []
        for review_data in Review.get_reviews():
            if review_data['user_id'] == self.user_id:
                review = Review(**review_data)
                self.reviews.append(review)

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