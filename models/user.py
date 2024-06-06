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