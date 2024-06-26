import unittest
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from persistence.datamanager import DataManager
from models.place import Place

class TestPlace(unittest.TestCase):
	def setUp(self):
		"""
		Set up a DataManager instance with a specific file path for storing JSON data.
		"""
		self.file_path = "test_places.json"
		self.datamanager = DataManager(self.file_path)

	def tearDown(self):
		"""
		Remove the JSON file after each test.
		"""
		if os.path.exists(self.file_path):
			os.remove(self.file_path)

	def test_place_crud(self):
		"""
		Test place CRUD operations.
		"""
		place = Place(
			name='Amazing Villa', 
			description='Beautiful villa with stunning views', 
			address='123 Main Street', 
			city_name='Cityville',
			latitude=40.7128, 
			longitude=-74.0060, 
			n_room=5, 
			n_bathroom=3,
			price_per_night=200.00, 
			n_max_people=10, 
			amenities='Pool, Wi-Fi, Parking',
			reviews='Great place!'
		)
		self.datamanager.create(place)

		retrieved_place = self.datamanager.read(place.id, Place)
		self.assertEqual(retrieved_place.name, 'Amazing Villa')
		self.assertEqual(retrieved_place.description, 'Beautiful villa with stunning views')
		self.assertEqual(retrieved_place.address, '123 Main Street')
		self.assertEqual(retrieved_place.city_name, 'Cityville')
		self.assertAlmostEqual(retrieved_place.latitude, 40.7128, places=4)
		self.assertAlmostEqual(retrieved_place.longitude, -74.0060, places=4)
		self.assertEqual(retrieved_place.n_room, 5)
		self.assertEqual(retrieved_place.n_bathroom, 3)
		self.assertEqual(retrieved_place.price_per_night, 200)
		self.assertEqual(retrieved_place.n_max_people, 10)
		self.assertEqual(retrieved_place.amenities, 'Pool, Wi-Fi, Parking')
		self.assertEqual(retrieved_place.reviews, 'Great place!')

		place.description = 'Updated description'
		self.datamanager.update(place)
		updated_place = self.datamanager.read(place.id, Place)
		self.assertEqual(updated_place.description, 'Updated description')

		self.datamanager.delete(place.id, Place)
		deleted_place = self.datamanager.read(place.id, Place)
		self.assertIsNone(deleted_place)

if __name__ == '__main__':
	unittest.main()
