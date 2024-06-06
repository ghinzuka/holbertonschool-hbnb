from uuid import UUID, uuid4
from datetime import datetime

class Review:
    def __init__(self, user_id: UUID, place_id: UUID, text: str, rating: int):
        self.review_id = uuid4()
        self.user_id = user_id
        self.place_id = place_id
        self.text = text
        self.rating = rating
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
