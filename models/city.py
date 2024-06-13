from .base import BaseModel


class City(BaseModel):
    def __init__(self, name: str, country_code: str):
        super().__init__()
        self.name = name
        self.country_code = country_code

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        if not isinstance(value, str) or not value:
            raise TypeError("City name must be a non-empty string")
        self._name = value

    @property
    def country_code(self):
        return self._country_code

    @country_code.setter
    def country_code(self, value: str):
        if not isinstance(value, str) or len(value) != 2:
            raise TypeError("Country code must be a 2-character string")
        self._country_code = value.upper()

    def to_dict(self):
        city_dict = {
            "name": self.name,
            "country_code": self.country_code
        }
        city_dict.update(super().to_dict())
        return city_dict

    @classmethod
    def from_dict(cls, data):
        instance = cls(
            name=data["name"],
            country_code=data["country_code"]
        )
        base_instance = BaseModel.from_dict(data)
        instance.id = base_instance.id
        instance.created_at = base_instance.created_at
        instance.updated_at = base_instance.updated_at
        return instance
