import unittest

from country import Country
from city import City

class TestCountry(unittest.TestCase):

    def setUp(self):
        # This will run before every test
        City._cities = {}  # Reset the class variable to ensure tests are isolated

    def test_create_country(self):
        country = Country("France")
        self.assertEqual(country.name, "France")
        self.assertEqual(country.cities, [])
    
    def test_add_city(self):
        country = Country("France")
        city = City("Paris")
        country.add_city(city)
        self.assertIn(city, country.cities)
    
    def test_add_duplicate_city(self):
        country = Country("France")
        city = City("Paris")
        country.add_city(city)
        with self.assertRaises(ValueError):
            country.add_city(city)
    
    def test_get_all_cities(self):
        country = Country("France")
        city1 = City("Paris")
        city2 = City("Lyon")
        country.add_city(city1)
        country.add_city(city2)
        all_cities = country.get_all_cities()
        self.assertIn(city1, all_cities)
        self.assertIn(city2, all_cities)
        self.assertEqual(len(all_cities), 2)

if __name__ == '__main__':
    unittest.main()
