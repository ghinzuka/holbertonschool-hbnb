import unittest
import os
import json
from models.city import City
from persistence.datamanager import DataManager


class TestCityCRUD(unittest.TestCase):
	"""
	Test case class for testing the CRUD operations of the City class.
	"""

	def setUp(self):
		self.db_path = 'tests/test_db.json'
		self.countries_temp_path = 'tests/test_countries.json'

		with open('persistence/countries.json', 'r') as src_file:
			countries_data = json.load(src_file)

		with open(self.countries_temp_path, 'w') as file:
			json.dump(countries_data, file)

		with open(self.db_path, 'w') as file:
			json.dump({}, file)

		self.data_manager = DataManager(self.db_path, self.countries_temp_path)

	def tearDown(self):
		os.remove(self.db_path)
		os.remove(self.countries_temp_path)

	def test_create_city(self):
		city = City(name="New York", country_code="US")
		self.data_manager.create_city(city)
		self.assertIn(f"{city.id}_City", self.data_manager.data)

	def test_read_city(self):
		city = City(name="Paris", country_code="FR")
		self.data_manager.create_city(city)
		read_city = self.data_manager.read_city(city.id)
		self.assertEqual(read_city.name, "Paris")

	def test_update_city(self):
		city = City(name="Berlin", country_code="DE")
		self.data_manager.create_city(city)
		city.name = "Munich"
		self.data_manager.update_city(city)
		updated_city = self.data_manager.read_city(city.id)
		self.assertEqual(updated_city.name, "Munich")

	def test_delete_city(self):
		city = City(name="San Francisco", country_code="US")
		self.data_manager.create_city(city)
		self.data_manager.delete_city(city.id)
		self.assertIsNone(self.data_manager.read_city(city.id))


if __name__ == '__main__':
    unittest.main()
