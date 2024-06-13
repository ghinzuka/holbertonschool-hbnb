import unittest
from models.city import City
from persistence.city_manager import CityManager

class TestCityManager(unittest.TestCase):
    
    def setUp(self):
        self.manager = CityManager()
        self.city = City(name="Test City", country_code="FR")

    def test_create_city(self):
        self.manager.create_city(self.city)
        city_key = f"{self.city.id}_City"
        self.assertIn(city_key, self.manager.cities)
        self.assertEqual(self.manager.cities[city_key]["name"], self.city.name)
        self.assertEqual(self.manager.cities[city_key]["country_code"], self.city.country_code)
        
    def test_read_city(self):
        self.manager.create_city(self.city)
        city_from_manager = self.manager.read_city(self.city.id)
        self.assertIsNotNone(city_from_manager)
        self.assertEqual(city_from_manager.name, self.city.name)
        self.assertEqual(city_from_manager.country_code, self.city.country_code)
        
    def test_update_city(self):
        self.manager.create_city(self.city)
        self.city.name = "Updated City"
        self.manager.update_city(self.city)
        city_from_manager = self.manager.read_city(self.city.id)
        self.assertEqual(city_from_manager.name, "Updated City")
        
    def test_delete_city(self):
        self.manager.create_city(self.city)
        self.manager.delete_city(self.city.id)
        city_from_manager = self.manager.read_city(self.city.id)
        self.assertIsNone(city_from_manager)
        
    def test_read_nonexistent_city(self):
        city_from_manager = self.manager.read_city("nonexistent_id")
        self.assertIsNone(city_from_manager)
        
    def test_update_nonexistent_city(self):
        non_existent_city = City(name="Nonexistent City", country_code="US")
        non_existent_city.id = "nonexistent_id"
        with self.assertRaises(ValueError):
            self.manager.update_city(non_existent_city)
        
    def test_delete_nonexistent_city(self):
        result = self.manager.delete_city("nonexistent_id")
        self.assertIsNone(result)

if __name__ == "__main__":
    unittest.main()
