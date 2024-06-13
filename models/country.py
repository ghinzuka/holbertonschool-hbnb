from .base import BaseModel

class Country(BaseModel):
    def __init__(self, code: str, name: str):
        self.code = code
        self.name = name

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value: str):
        if not isinstance(value, str) or len(value) != 2:
            raise TypeError("Country code must be a 2-character string")
        self._code = value.upper()

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        if not isinstance(value, str) or not value:
            raise TypeError("Country name must be a non-empty string")
        self._name = value

    def to_dict(self):
        return {
            "code": self.code,
            "name": self.name
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            code=data["code"],
            name=data["name"]
        )
