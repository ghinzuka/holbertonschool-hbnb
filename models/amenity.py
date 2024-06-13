from .base import BaseModel


class Amenities(BaseModel):
    """
    Represents an amenity.

    Attributes:
            name (str): The name of the amenity.
    """

    def __init__(self, name: str):
        super().__init__()
        self.name = name

    @property
    def name(self):
        """
        Getter method for the name attribute.

        Returns:
                str: The name of the amenity.
        """
        return self._name

    @name.setter
    def name(self, value):
        """
        Setter method for the name attribute.

        Args:
                value (str): The name of the amenity.

        Raises:
                TypeError: If the value is not a non-empty string.
        """
        if not isinstance(value, str) or not value:
            raise TypeError("name must be a non-empty string")
        self._name = value

    def to_dict(self):
        """
        Converts the amenity object to a dictionary.

        Returns:
                dict: A dictionary representation of the amenity object.
        """
        amenities_dict = super().to_dict()
        amenities_dict.update({
            "name": self.name
        })
        return amenities_dict

    @classmethod
    def from_dict(cls, data):
        """
        Creates an amenity object from a dictionary.

        Args:
                data (dict): A dictionary containing the amenity data.

        Returns:
                Amenities: An instance of the Amenities class.
        """
        instance = cls(
            name=data["name"]
        )
        base_instance = BaseModel.from_dict(data)
        instance.id = base_instance.id
        instance.created_at = base_instance.created_at
        instance.updated_at = base_instance.updated_at
        return instance
