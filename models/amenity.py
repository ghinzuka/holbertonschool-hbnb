from .base import BaseModel

class Amenities(BaseModel):
    def __init__(self, name: str):
        super().__init__()
        self.name = name 

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not value:
            raise TypeError("name must be a non-empty string")
        self.__name = value

    def to_dict(self):
        return {
            "name": self.name,
            "id": self.id
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            name=data["name"]
            )