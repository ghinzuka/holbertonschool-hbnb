import unittest
from city import City
from datetime import datetime

class TestCity(unittest.TestCase):

    def setUp(self):
        # This will run before every test
        City._cities = {}  # Reset the class variable to ensure tests are isolated

    def test_create_city(self):
        city = City("Paris")
        self.assertEqual(city.name, "Paris")
        self.assertIsNotNone(city.city_id)
        self.assertIsNotNone(city.created_at)
        self.assertIsNotNone(city.updated_at)
    
    def test_get_all_cities(self):
        city1 = City("Paris")
        city2 = City("Lyon")
        all_cities = list(City.get_all_cities())
        self.assertIn(city1, all_cities)
        self.assertIn(city2, all_cities)
        self.assertEqual(len(all_cities), 2)

    def test_existing_city(self):
        city1 = City("Paris")
        city2 = City("Paris")
        self.assertEqual(city1.city_id, city2.city_id)
        self.assertEqual(city1.created_at, city2.created_at)
        # Round to ignore microsecond differences
        self.assertAlmostEqual(city1.updated_at.timestamp(), city2.updated_at.timestamp(), places=0)

if __name__ == '__main__':
    unittest.main() 