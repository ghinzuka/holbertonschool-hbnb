import unittest
from amenity import Amenities
from datetime import datetime

class TestAmenities(unittest.TestCase):

    def setUp(self):
        # Clear the amenities dictionary before each test
        Amenities._amenities.clear()

    def test_create_amenity(self):
        amenity_name = "WiFi"
        amenity = Amenities(name=amenity_name)

        self.assertEqual(amenity.name, amenity_name)
        self.assertIsNotNone(amenity.amenity_id)
        self.assertIsInstance(amenity.created_at, datetime)
        self.assertIsInstance(amenity.updated_at, datetime)
        self.assertIn(amenity_name, Amenities._amenities)

    def test_create_duplicate_amenity(self):
        amenity_name = "WiFi"
        Amenities(name=amenity_name)

        with self.assertRaises(ValueError):
            Amenities(name=amenity_name)

    def test_get_all_amenities(self):
        amenity1 = Amenities(name="WiFi")
        amenity2 = Amenities(name="Pool")
        
        all_amenities = list(Amenities.get_all_amenities())
        
        self.assertIn(amenity1, all_amenities)
        self.assertIn(amenity2, all_amenities)
        self.assertEqual(len(all_amenities), 2)

if __name__ == '__main__':
    unittest.main()
