import unittest

from city import City

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
    
    def test_create_duplicate_city(self):
        City("Paris")
        with self.assertRaises(ValueError):
            City("Paris")
    
    def test_get_all_cities(self):
        city1 = City("Paris")
        city2 = City("Lyon")
        all_cities = list(City.get_all_cities())
        self.assertIn(city1, all_cities)
        self.assertIn(city2, all_cities)
        self.assertEqual(len(all_cities), 2)

if __name__ == '__main__':
    unittest.main()
