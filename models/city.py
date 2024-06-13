from .base import BaseModel

class City(BaseModel):
	"""Represents a city.

	Attributes:
		name (str): The name of the city.
		country_code (str): The country code of the city.
	"""

	def __init__(self, name: str, country_code: str):
		super().__init__()
		self.name = name
		self.country_code = country_code

	@property
	def name(self):
		"""str: The name of the city."""
		return self._name

	@name.setter
	def name(self, value: str):
		"""Set the name of the city.

		Args:
			value (str): The name of the city.

		Raises:
			TypeError: If the name is not a non-empty string.
		"""
		if not isinstance(value, str) or not value:
			raise TypeError("City name must be a non-empty string")
		self._name = value

	@property
	def country_code(self):
		"""str: The country code of the city."""
		return self._country_code

	@country_code.setter
	def country_code(self, value: str):
		"""Set the country code of the city.

		Args:
			value (str): The country code of the city.

		Raises:
			TypeError: If the country code is not a 2-character string.
		"""
		if not isinstance(value, str) or len(value) != 2:
			raise TypeError("Country code must be a 2-character string")
		self._country_code = value.upper()

	def to_dict(self):
		"""Converts the City instance to a dictionary.

		Returns:
			dict: A dictionary representation of the City instance.
		"""
		city_dict = {
			"name": self.name,
			"country_code": self.country_code
		}
		city_dict.update(super().to_dict())
		return city_dict

	@classmethod
	def from_dict(cls, data):
		"""Creates a City instance from a dictionary.

		Args:
			data (dict): A dictionary containing the City data.

		Returns:
			City: A new City instance created from the dictionary.
		"""
		instance = cls(
			name=data["name"],
			country_code=data["country_code"]
		)
		base_instance = BaseModel.from_dict(data)
		instance.id = base_instance.id
		instance.created_at = base_instance.created_at
		instance.updated_at = base_instance.updated_at
		return instance
