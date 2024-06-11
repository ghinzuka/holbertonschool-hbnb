from .base import BaseModel

class Review(BaseModel):
    def __init__(self, text: str, rating: int):
        super().__init__()
        self.text = text
        self.rating = rating

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
