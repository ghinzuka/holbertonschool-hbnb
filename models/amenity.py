from .base import BaseModel

class Amenities(BaseModel):
    def __init__(self, name: str):
        super().__init__()
        self.name = name 

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not value:
            raise TypeError("name must be a non-empty string")
        self._name = value

    def to_dict(self):
        amenities_dict = super().to_dict()  # Inclure les attributs de BaseModel
        amenities_dict.update({
            "name": self.name
        })
        return amenities_dict

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