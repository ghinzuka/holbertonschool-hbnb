from .base import BaseModel


class Country(BaseModel):
    """Represents a country with a code and name."""

    def __init__(self, code: str, name: str):
        self.code = code
        self.name = name

    @property
    def code(self):
        """Get the country code."""
        return self._code

    @code.setter
    def code(self, value: str):
        """Set the country code.

        Args:
                value (str): The country code.

        Raises:
                TypeError: If the value is not a 2-character string.
        """
        if not isinstance(value, str) or len(value) != 2:
            raise TypeError("Country code must be a 2-character string")
        self._code = value.upper()

    @property
    def name(self):
        """Get the country name."""
        return self._name

    @name.setter
    def name(self, value: str):
        """Set the country name.

        Args:
                value (str): The country name.

        Raises:
                TypeError: If the value is not a non-empty string.
        """
        if not isinstance(value, str) or not value:
            raise TypeError("Country name must be a non-empty string")
        self._name = value

    def to_dict(self):
        """Convert the country object to a dictionary.

        Returns:
                dict: A dictionary representation of the country object.
        """
        return {
            "code": self.code,
            "name": self.name
        }

    @classmethod
    def from_dict(cls, data):
        """Create a country object from a dictionary.

        Args:
                data (dict): A dictionary containing the country data.

        Returns:
                Country: A new country object created from the dictionary.
        """
        return cls(
            code=data["code"],
            name=data["name"]
        )
