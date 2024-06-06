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

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if not isinstance(value, str) or not value:
            raise TypeError("email must be a non-empty string")
        # Basic email format validation using regex
        email_pattern = re.compile(r"[^@]+@[^@]+\.[^@]+")
        if not email_pattern.match(value):
            raise ValueError("invalid email format")
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