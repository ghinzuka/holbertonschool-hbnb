import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models.user import User
from persistence.datamanager import DataManager

class TestUser(unittest.TestCase):
	def setUp(self):
		"""
		Set up a DataManager instance with a specific file path for storing JSON data.
		"""
		self.file_path = "test_users.json" 
		self.datamanager = DataManager(self.file_path)

	def tearDown(self):
		"""
		Remove the JSON file after each test.
		"""
		if os.path.exists(self.file_path):
			os.remove(self.file_path)

	def test_user_crud(self):
		"""
		Test user CRUD operations.
		"""
		user = User(email='email@example.com', password='password', first_name='John', last_name='Doe')
		self.datamanager.create(user)

		retrieved_user = self.datamanager.read(user.id, User)
		self.assertEqual(retrieved_user.email, 'email@example.com')
		self.assertEqual(retrieved_user.password, 'password')
		self.assertEqual(retrieved_user.first_name, 'John')
		self.assertEqual(retrieved_user.last_name, 'Doe')
		self.assertIsNotNone(retrieved_user.id)

		user.first_name = 'Jane'
		self.datamanager.update(user)
		updated_user = self.datamanager.read(user.id, User)
		self.assertEqual(updated_user.first_name, 'Jane')

		self.datamanager.delete(user.id, User)
		deleted_user = self.datamanager.read(user.id, User)
		self.assertIsNone(deleted_user)

if __name__ == '__main__':
	unittest.main()