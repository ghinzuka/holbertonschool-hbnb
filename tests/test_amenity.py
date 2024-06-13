from models.amenity import Amenities
from persistence.datamanager import DataManager
import unittest
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class TestAmenities(unittest.TestCase):
    def setUp(self):
        """
        Create an instance of DataManager with a specific file path for storing JSON data
        """
        self.file_path = "test_amenities.json"
        self.datamanager = DataManager(self.file_path)

    def tearDown(self):
        """
        Remove the JSON file after each test
        """
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_amenities_crud(self):
        """
        Test CRUD operations for amenities
        """
        amenities = Amenities(name='Swimming Pool')
        self.datamanager.create(amenities)

        retrieved_amenities = self.datamanager.read(amenities.id, Amenities)
        self.assertEqual(retrieved_amenities.name, 'Swimming Pool')
        self.assertIsNotNone(retrieved_amenities.id)

        amenities.name = 'Gym'
        self.datamanager.update(amenities)
        updated_amenities = self.datamanager.read(amenities.id, Amenities)
        self.assertEqual(updated_amenities.name, 'Gym')

        self.datamanager.delete(amenities.id, Amenities)
        deleted_amenities = self.datamanager.read(amenities.id, Amenities)
        self.assertIsNone(deleted_amenities)


if __name__ == '__main__':
    unittest.main()
