import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from persistence.datamanager import DataManager
from models.amenity import Amenities

class TestAmenity(unittest.TestCase):
    def setUp(self):
        self.datamanager = DataManager(MockStorage())

    def test_amenity_crud(self):
        # Création d'un équipement
        amenity = Amenities("Pool")
        self.datamanager.create(amenity)

        # Récupération de l'équipement
        retrieved_amenity = self.datamanager.read(amenity.id, Amenities)
        self.assertEqual(retrieved_amenity.name, "Pool")

        # Mise à jour de l'équipement
        amenity.name = "Updated Amenity"
        self.datamanager.update(amenity)
        updated_amenity = self.datamanager.read(amenity.id, Amenities)
        self.assertEqual(updated_amenity.name, "Updated Amenity")

        # Suppression de l'équipement
        self.datamanager.delete(amenity.id, Amenities)
        deleted_amenity = self.datamanager.read(amenity.id, Amenities)
        self.assertIsNone(deleted_amenity)

class MockStorage:
    def __init__(self):
        self.data = {}

    def create(self, entity):
        self.data[(entity.id, type(entity))] = entity

    def read(self, entity_id, entity_type):
        return self.data.get((entity_id, entity_type))

    def update(self, entity):
        self.data[(entity.id, type(entity))] = entity

    def delete(self, entity_id, entity_type):
        del self.data[(entity_id, entity_type)]

if __name__ == '__main__':
    unittest.main()
