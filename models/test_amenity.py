import unittest
from uuid import UUID
from datetime import datetime
from amenity import Amenities

class TestAmenities(unittest.TestCase):


    def test_add_amenities(self):
        names = ["Pool", "Gym", "WiFi"]
        amenities = Amenities(names)
        self.assertEqual(len(Amenities._amenities), 3)
        self.assertEqual(Amenities._amenities[0]['name'], "Pool")
        self.assertEqual(Amenities._amenities[1]['name'], "Gym")
        self.assertEqual(Amenities._amenities[2]['name'], "WiFi")

    def test_amenity_ids_are_unique(self):
        names = ["Pool", "Gym"]
        amenities = Amenities(names)
        amenity_ids = [amenity['amenity_id'] for amenity in Amenities._amenities]
        self.assertEqual(len(set(amenity_ids)), len(amenity_ids))
        for amenity in Amenities._amenities:
            self.assertIsInstance(amenity['amenity_id'], UUID)

    def test_created_and_updated_at(self):
        names = ["Pool", "Gym"]
        amenities = Amenities(names)
        for amenity in Amenities._amenities:
            self.assertIsInstance(amenity['created_at'], datetime)
            self.assertIsInstance(amenity['updated_at'], datetime)

    def test_duplicate_amenity_names(self):
        names = ["Pool", "Gym"]
        Amenities(names)
        with self.assertRaises(ValueError):
            Amenities(["Pool"])

    def test_invalid_amenity_name_type(self):
        with self.assertRaises(TypeError):
            Amenities([123, "Gym"])

    def test_get_all_amenities(self):
        names = ["Pool", "Gym"]
        amenities = Amenities(names)
        all_amenities = Amenities.get_all_amenities()
        self.assertEqual(len(all_amenities), 2)

    def test_get_amenities_by_name(self):
        names = ["Pool", "Gym", "WiFi"]
        amenities = Amenities(names)
        pool_amenities = Amenities.get_amenities_by_name("Pool")
        self.assertEqual(len(pool_amenities), 1)
        self.assertEqual(pool_amenities[0]['name'], "Pool")

    def test_add_duplicate_names(self):
        names = ["Pool", "Gym", "Pool"]
        amenities = Amenities(names)
        self.assertEqual(len(Amenities._amenities), 2)

    def test_add_existing_amenity_name(self):
        Amenities(["Pool", "Gym"])
        Amenities(["Pool", "WiFi"])
        self.assertEqual(len(Amenities._amenities), 3)
        existing_amenity = next((amenity for amenity in Amenities._amenities if amenity['name'] == "Pool"), None)
        self.assertIsNotNone(existing_amenity)
        self.assertEqual(existing_amenity['name'], "Pool")

if __name__ == '__main__':
    unittest.main()
