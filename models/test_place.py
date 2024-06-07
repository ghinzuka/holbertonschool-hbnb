import unittest
from uuid import uuid4
from datetime import datetime
from city import City
from amenity import Amenities
from review import Review
from country import Country
from place import Place

class TestPlace(unittest.TestCase):
    def setUp(self):
        self.city = City("TestCity")
        self.country = Country("TestCountry", [self.city])
        self.amenities = Amenities(["wifi", "piscine"])  # Pass a list of amenities
        self.review = Review(uuid4(), uuid4(), "Great place!", 5)
        self.place = Place("Test Place", "Test description", "Test address", "TestCity", 
                           10.0, 20.0, uuid4(), uuid4(), 2, 1, 100.0, 4, 
                           self.amenities, [self.review], self.country)

    def test_creation(self):
        self.assertEqual(self.place.name, "Test Place")
        self.assertEqual(self.place.description, "Test description")
        self.assertEqual(self.place.address, "Test address")
        self.assertEqual(self.place.city_name, "TestCity")
        self.assertEqual(self.place.latitude, 10.0)
        self.assertEqual(self.place.longitude, 20.0)
        self.assertIsInstance(self.place.user_id, uuid4)
        self.assertIsInstance(self.place.creator_id, uuid4)
        self.assertEqual(self.place.n_room, 2)
        self.assertEqual(self.place.n_bathroom, 1)
        self.assertEqual(self.place.price_per_night, 100.0)
        self.assertEqual(self.place.n_max_people, 4)
        self.assertEqual(self.place.amenities, self.amenities)
        self.assertEqual(self.place.reviews, [self.review])
        self.assertIsInstance(self.place.created_at, datetime)
        self.assertIsInstance(self.place.updated_at, datetime)

    def test_update(self):
        self.place.update(self.place.creator_id, name="Updated Place")
        self.assertEqual(self.place.name, "Updated Place")

        with self.assertRaises(PermissionError):
            self.place.update(uuid4(), name="Attempted Update")

if __name__ == '__main__':
    unittest.main()