import unittest
from uuid import UUID, uuid4
from datetime import datetime
from user import User

class TestUser(unittest.TestCase):

    def setUp(self):
        User._registered_emails.clear()

    def test_user_creation(self):
        user = User(email="test@example.com", password="password", first_name="John", last_name="Doe")
        self.assertIsInstance(user.user_id, UUID)
        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(user.password, "password")
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")
        self.assertIsInstance(user.created_at, datetime)
        self.assertIsInstance(user.updated_at, datetime)

    def test_unique_email_constraint(self):
        user1 = User(email="unique@example.com", password="password", first_name="John", last_name="Doe")
        with self.assertRaises(ValueError) as context:
            user2 = User(email="unique@example.com", password="password", first_name="Jane", last_name="Doe")
        self.assertEqual(str(context.exception), "Email unique@example.com is already taken.")

    def test_user_update(self):
        user = User(email="test_update@example.com", password="password", first_name="John", last_name="Doe")
        user.update(first_name="Jane", email="test_updated@example.com")
        self.assertEqual(user.first_name, "Jane")
        self.assertEqual(user.email, "test_updated@example.com")

    def test_duplicate_email_registration(self):
        user1 = User(email="duplicate@example.com", password="password", first_name="John", last_name="Doe")
        with self.assertRaises(ValueError) as context:
            user2 = User(email="duplicate@example.com", password="password", first_name="Jane", last_name="Smith")
        self.assertEqual(str(context.exception), "Email duplicate@example.com is already taken.")

if __name__ == '__main__':
    unittest.main()
