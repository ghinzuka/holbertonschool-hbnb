import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models.base import BaseModel
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenities
from models.city import City
from models.country import Country

class TestModels(unittest.TestCase):
    """
	This class contains unit tests for the models in the application.
	"""
    def test_user_creation(self):
        user = User('email@example.com', 'password', 'John', 'Doe')
        self.assertIsNotNone(user.id)
        self.assertEqual(user.email, 'email@example.com')
        self.assertEqual(user.password, 'password')
        self.assertEqual(user.first_name, 'John')
        self.assertEqual(user.last_name, 'Doe')
        self.assertIsNotNone(user.created_at)
        self.assertIsNotNone(user.updated_at)

    def test_place_creation(self):
        place = Place('Test Place', 'Description', 'Address', 'City Name', 40.7128, -74.0060, 3, 2, 150.0, 4, 'amenities', 'reviews')
        self.assertIsNotNone(place.id)
        self.assertEqual(place.name, 'Test Place')
        self.assertEqual(place.description, 'Description')
        self.assertEqual(place.address, 'Address')
        self.assertEqual(place.city_name, 'City Name')
        self.assertEqual(place.latitude, 40.7128)
        self.assertEqual(place.longitude, -74.0060)
        self.assertEqual(place.n_room, 3)
        self.assertEqual(place.n_bathroom, 2)
        self.assertEqual(place.price_per_night, 150.0)
        self.assertEqual(place.n_max_people, 4)
        self.assertEqual(place.amenities, 'amenities')
        self.assertEqual(place.reviews, 'reviews')
        self.assertIsNotNone(place.created_at)
        self.assertIsNotNone(place.updated_at)

    def test_review_creation(self):
        review = Review('Great place!', 5)
        self.assertIsNotNone(review.id)
        self.assertEqual(review.text, 'Great place!')
        self.assertEqual(review.rating, 5)
        self.assertIsNotNone(review.created_at)
        self.assertIsNotNone(review.updated_at)

    def test_amenity_creation(self):
        amenity = Amenities("Pool")
        self.assertEqual(amenity.name, "Pool")

    def test_city_creation(self):
        city = City('New York')
        self.assertIsNotNone(city.id)
        self.assertEqual(city.name, 'New York')
        self.assertIsNotNone(city.created_at)
        self.assertIsNotNone(city.updated_at)

    def test_country_creation(self):
        city = City('New York')
        country = Country(city, 'USA')
        self.assertIsNotNone(country.id)
        self.assertEqual(country.name, 'USA')
        self.assertEqual(country.city, city)
        self.assertIsNotNone(country.created_at)
        self.assertIsNotNone(country.updated_at)

    def test_base_model(self):
        base = BaseModel()
        self.assertIsNotNone(base.id)
        self.assertIsNotNone(base.created_at)
        self.assertIsNotNone(base.updated_at)
        base.save()
        self.assertNotEqual(base.created_at, base.updated_at)

if __name__ == '__main__':
    unittest.main()
