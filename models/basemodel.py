from uuid import uuid4
from datetime import datetime

class BaseModel:
    def __init__(self):
        self.id = uuid4()
        self.created_at = datetime.now()
        self.updated_at = datetime.now()