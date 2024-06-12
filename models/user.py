from .base import BaseModel

class User(BaseModel):
    def __init__(
            self,
            email: str,
            password: str,
            first_name: str,
            last_name: str):
        super().__init__()
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if not isinstance(value, str) or not value:
            raise TypeError("email must be a non-empty string")
        self._email = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        if not isinstance(value, str) or not value:
            raise TypeError("password must be a non-empty string")
        self._password = value

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str) or not value:
            raise TypeError("first_name must be a non-empty string")
        self._first_name = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        if not isinstance(value, str) or not value:
            raise TypeError("last_name must be a non-empty string")
        self._last_name = value
    
    def to_dict(self):
        user_dict = super().to_dict()  # Inclure les champs de BaseModel
        user_dict.update({
            "email": self.email,
            "password": self.password,
            "first_name": self.first_name,
            "last_name": self.last_name
        })
        return user_dict

    @classmethod
    def from_dict(cls, data):
        instance = cls(
            email=data["email"],
            password=data["password"],
            first_name=data["first_name"],
            last_name=data["last_name"]
        )
        base_instance = BaseModel.from_dict(data)
        instance.id = base_instance.id
        instance.created_at = base_instance.created_at
        instance.updated_at = base_instance.updated_at
        return instance