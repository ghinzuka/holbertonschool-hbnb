import unittest
from uuid import UUID
from datetime import datetime
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models.city import City 

class TestCity(unittest.TestCase):
    
    def setUp(self):
        City._cities = []
    
    def test_create_city(self):
        city = City("Paris")
        self.assertEqual(city.name, "Paris")
        self.assertIsInstance(city.city_id, UUID)
        self.assertIsInstance(city.created_at, datetime)
        self.assertIsInstance(city.updated_at, datetime)
        self.assertEqual(len(City.get_all_cities()), 1)
    
    def test_get_city_by_name(self):
        City("Paris")
        city = City.get_city_by_name("Paris")
        self.assertIsNotNone(city)
        self.assertEqual(city['name'], "Paris")
    
    def test_create_duplicate_city(self):
        City("Paris")
        with self.assertRaises(ValueError):
            City("Paris")
    
    def test_update_city(self):
        city = City("Los Angeles")
        city.update(name="LA")
        updated_city = City.get_city_by_name("LA")
        self.assertIsNotNone(updated_city)
        self.assertEqual(updated_city['name'], "LA")
        self.assertNotEqual(updated_city['updated_at'], updated_city['created_at'])
    
    def test_get_all_cities(self):
        City("Paris")
        City("New York")
        cities = City.get_all_cities()
        self.assertEqual(len(cities), 2)
        city_names = [city['name'] for city in cities]
        self.assertIn("Paris", city_names)
        self.assertIn("New York", city_names)

if __name__ == "__main__":
    unittest.main()
