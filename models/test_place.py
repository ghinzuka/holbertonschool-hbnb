# TestPlace.py
import unittest
from uuid import UUID, uuid4
from datetime import datetime
from place import Place
from city import City
from country import Country
from review import Review
from amenity import Amenities

class TestPlace(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Clear the created cities before each test to ensure isolation
        City._cities.clear()

    def setUp(self):
        # Create a unique city for each test
        self.city = City(name=f"Test City {uuid4()}")
        self.country = Country(name="Test Country", cities=[self.city])

    def test_place_creation(self):
        place = Place(
            name="Test Place",
            description="A nice place to stay",
            address="1234 Main St, Test City, Test State, 12345",  # Corrected address format
            city_name=self.city.name,
            latitude=40.7128,
            longitude=-74.0060,
            user_id=uuid4(),
            creator_id=uuid4(),
            n_room=2,
            n_bathroom=1,
            price_per_night=100.0,
            n_max_people=4,
            amenities=Amenities(name="WiFi"),
            reviews=[],
            country=self.country
        )
        self.assertIsInstance(place.place_id, UUID)
        self.assertEqual(place.name, "Test Place")
        self.assertEqual(place.description, "A nice place to stay")
        self.assertEqual(place.address, "1234 Main St, Test City, Test State, 12345")
        self.assertEqual(place.city_name, self.city.name)
        self.assertEqual(place.latitude, 40.7128)
        self.assertEqual(place.longitude, -74.0060)
        self.assertEqual(place.n_room, 2)
        self.assertEqual(place.n_bathroom, 1)
        self.assertEqual(place.price_per_night, 100.0)
        self.assertEqual(place.n_max_people, 4)
        self.assertEqual(place.amenities.name, "WiFi")
        self.assertEqual(place.reviews, [])
        self.assertIsInstance(place.created_at, datetime)
        self.assertIsInstance(place.updated_at, datetime)

    def test_adding_review(self):
        place = Place(
            name="Test Place",
            description="A nice place to stay",
            address="1234 Main St, Test City, Test State, 12345",
            city_name=self.city.name,
            latitude=40.7128,
            longitude=-74.0060,
            user_id=uuid4(),
            creator_id=uuid4(),
            n_room=2,
            n_bathroom=1,
            price_per_night=100.0,
            n_max_people=4,
            amenities=Amenities(name="WiFi"),  # Corrected to use existing amenity
            reviews=[],
            country=self.country
        )
        review = Review(user_id=uuid4(), place_id=place.place_id, text="Great place!", rating=5)
        place.reviews.append(review)
        self.assertIn(review, place.reviews)

if __name__ == '__main__':
    unittest.main()
