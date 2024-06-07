import unittest
from datetime import datetime
from uuid import UUID, uuid4
from city import City
from country import Country
from review import Review
from place import Place

class TestPlace(unittest.TestCase):
    def setUp(self):
        # Create some test data
        self.city = City("Test City")
        self.country = Country("Test Country", [self.city])
        self.user_id = uuid4()
        self.creator_id = uuid4()
        self.amenities = ["Wifi", "Pool"]
        self.reviews = [Review(uuid4(), uuid4(), "Great place!", 5), 
                        Review(uuid4(), uuid4(), "Nice location", 4)]
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
        print("Name:", self.place.name)
        print("Description:", self.place.description)
        print("Address:", self.place.address)
        print("City Name:", self.place.city_name)
        print("Latitude:", self.place.latitude)
        print("Longitude:", self.place.longitude)
        print("User ID:", self.place.user_id)
        print("Creator ID:", self.place.creator_id)
        print("Number of Rooms:", self.place.n_room)
        print("Number of Bathrooms:", self.place.n_bathroom)
        print("Price per Night:", self.place.price_per_night)
        print("Maximum People:", self.place.n_max_people)
        print("Amenities:", self.place.amenities)
        print("Reviews:", self.place.reviews)
        print("Created At:", self.place.created_at)
        print("Updated At:", self.place.updated_at)

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
        self.assertEqual(self.place.reviews, self.reviews)
        self.assertIsInstance(self.place.created_at, datetime)
        self.assertIsInstance(self.place.updated_at, datetime)

if __name__ == '__main__':
    unittest.main()
