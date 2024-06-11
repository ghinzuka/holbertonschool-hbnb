import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models.place import Place
from persistence.datamanager import DataManager

class TestPlace(unittest.TestCase):
    def setUp(self):
        # Créer une instance de DataManager avec un stockage fictif pour les tests
        self.datamanager = DataManager(MockStorage())

    def test_place_crud(self):
        # Création d'un lieu
        place = Place('Test Place', 'Description', 'Address', 'City Name', 40.7128, -74.0060, 3, 2, 150.0, 4, 'amenities', 'reviews')
        self.datamanager.create(place)

        # Récupération du lieu
        retrieved_place = self.datamanager.read(place.id, Place)
        self.assertEqual(retrieved_place.name, 'Test Place')
        self.assertEqual(retrieved_place.description, 'Description')
        self.assertEqual(retrieved_place.address, 'Address')
        self.assertEqual(retrieved_place.city_name, 'City Name')
        self.assertEqual(retrieved_place.latitude, 40.7128)
        self.assertEqual(retrieved_place.longitude, -74.0060)

        # Mise à jour du lieu
        place.name = 'Updated Place'
        self.datamanager.update(place)
        updated_place = self.datamanager.read(place.id, Place)
        self.assertEqual(updated_place.name, 'Updated Place')

        # Suppression du lieu
        self.datamanager.delete(place.id, Place)
        deleted_place = self.datamanager.read(place.id, Place)
        self.assertIsNone(deleted_place)

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
