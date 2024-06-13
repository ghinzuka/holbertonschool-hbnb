from uuid import uuid4
from datetime import datetime

class BaseModel:
	"""
	Base class for all models in the application.

	Attributes:
		id (str): The unique identifier for the model instance.
		created_at (datetime): The date and time when the model instance was created.
		updated_at (datetime): The date and time when the model instance was last updated.
	"""

	def __init__(self):
		self.id = str(uuid4())
		self.created_at = datetime.now()
		self.updated_at = datetime.now()

	def save(self):
		"""
		Updates the `updated_at` attribute with the current date and time.
		"""
		self.updated_at = datetime.now()

	def to_dict(self):
		"""
		Converts the model instance to a dictionary representation.

		Returns:
			dict: A dictionary containing the model instance's attributes.
		"""
		return {
			"id": self.id,
			"created_at": self.created_at.isoformat(),
			"updated_at": self.updated_at.isoformat()
		}

	@classmethod
	def from_dict(cls, data):
		"""
		Creates a new model instance from a dictionary representation.

		Args:
			data (dict): A dictionary containing the model instance's attributes.

		Returns:
			BaseModel: A new instance of the model class.
		"""
		instance = cls()
		instance.id = data.get("id", str(uuid4()))
		instance.created_at = datetime.fromisoformat(data["created_at"])
		instance.updated_at = datetime.fromisoformat(data["updated_at"])
		return instance
