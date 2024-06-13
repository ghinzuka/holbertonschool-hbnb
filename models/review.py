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

    def to_dict(self):
        review_dict = super().to_dict()  # Inclure les champs de BaseModel
        review_dict.update({
            "text": self.text,
            "rating": self.rating
        })
        return review_dict

    @classmethod
    def from_dict(cls, data):
        instance = cls(
            text=data["text"],
            rating=data["rating"]
        )
        base_instance = BaseModel.from_dict(data)
        instance.id = base_instance.id
        instance.created_at = base_instance.created_at
        instance.updated_at = base_instance.updated_at
        return instance