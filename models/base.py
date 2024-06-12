from uuid import uuid4
from datetime import datetime

class BaseModel:
    def __init__(self):
        self.id = str(uuid4())  # Initialiser l'UUID et le convertir en chaîne
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        return {
            "id": self.id,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }

    @classmethod
    def from_dict(cls, data):
        instance = cls()
        instance.id = data.get("id", str(uuid4()))
        instance.created_at = datetime.fromisoformat(data["created_at"])
        instance.updated_at = datetime.fromisoformat(data["updated_at"])
        return instance
