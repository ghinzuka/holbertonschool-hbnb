import unittest
<<<<<<< HEAD
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
        City._cities.clear()
        Amenities._amenities.clear()

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
            amenities=Amenities(name="WiFi"), 
            reviews=[],
            country=self.country
        )
        review = Review(user_id=uuid4(), place_id=place.place_id, text="Great place!", rating=5)
        place.reviews.append(review)
        self.assertIn(review, place.reviews)

if __name__ == '__main__':
    unittest.main()
=======
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
>>>>>>> Baptiste
