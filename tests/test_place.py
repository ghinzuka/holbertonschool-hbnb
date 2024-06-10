import unittest
from datetime import datetime
from uuid import UUID, uuid4
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models.city import City
from models.country import Country
from models.review import Review
from models.place import Place

class TestPlace(unittest.TestCase):
    def setUp(self):
        # Create some test data
        self.city = City("Test City")
        self.country = Country("Test Country", [self.city])
        self.user_id = uuid4()
        self.creator_id = uuid4()
        self.amenities = ["Wifi", "Pool"]
        self.review_user_id = uuid4()
        self.review_place_id = uuid4()
        self.review_text = "Great place!"
        self.review_rating = 5
        self.reviews = [Review(self.review_user_id, self.review_place_id, self.review_text, self.review_rating, [])]  # Updated with places_list parameter
        self.place = Place(
            "Test Place",
            "Test Description",
            "123 Test St",
            "Test City",
            40.7128,
            -74.0060,
            self.user_id,
            self.creator_id,
            2,
            1,
            100.0,
            4,
            self.amenities,
            self.reviews,
            self.country
        )

    def test_valid_place_creation(self):
        self.assertEqual(self.place.name, "Test Place")
        self.assertEqual(self.place.description, "Test Description")
        self.assertEqual(self.place.address, "123 Test St")
        self.assertEqual(self.place.city_name, "Test City")
        self.assertEqual(self.place.latitude, 40.7128)
        self.assertEqual(self.place.longitude, -74.0060)
        self.assertEqual(self.place.user_id, self.user_id)
        self.assertEqual(self.place.creator_id, self.creator_id)
        self.assertEqual(self.place.n_room, 2)
        self.assertEqual(self.place.n_bathroom, 1)
        self.assertEqual(self.place.price_per_night, 100.0)
        self.assertEqual(self.place.n_max_people, 4)
        self.assertEqual(self.place.amenities, self.amenities)
        self.assertEqual(len(self.place.reviews), 1)
        self.assertEqual(self.place.reviews[0].user_id, self.review_user_id)
        self.assertEqual(self.place.reviews[0].place_id, self.review_place_id)
        self.assertEqual(self.place.reviews[0].text, self.review_text)
        self.assertEqual(self.place.reviews[0].rating, self.review_rating)
        self.assertIsInstance(self.place.created_at, datetime)
        self.assertIsInstance(self.place.updated_at, datetime)

if __name__ == '__main__':
    unittest.main()
