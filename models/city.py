from .base import BaseModel

class City(BaseModel):
    def __init__(self, name: str):
        super().__init__()
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        if not isinstance(value, str) or not value:
            raise TypeError("name must be a non-empty string")
        self._name = value

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