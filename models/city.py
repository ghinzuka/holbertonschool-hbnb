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
        city_dict = {
            "name": self.name
        }
        city_dict.update(super().to_dict())  # Ajouter les attributs de BaseModel
        return city_dict

    @classmethod
    def from_dict(cls, data):
        instance = cls(
            name=data["name"]
        )
        base_instance = BaseModel.from_dict(data)
        instance.id = base_instance.id
        instance.created_at = base_instance.created_at
        instance.updated_at = base_instance.updated_at
        return instance