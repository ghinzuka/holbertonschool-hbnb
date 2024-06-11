import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from persistence.datamanager import DataManager
from models.city import City

class TestCity(unittest.TestCase):
    def setUp(self):
        # Créer une instance de DataManager avec un stockage fictif pour les tests
        self.datamanager = DataManager(MockStorage())

    def test_city_crud(self):
        # Création d'une ville
        city = City('New York')
        self.datamanager.create(city)

        # Récupération de la ville
        retrieved_city = self.datamanager.read(city.id, City)
        self.assertEqual(retrieved_city.name, 'New York')

        # Mise à jour de la ville
        city.name = 'Updated City'
        self.datamanager.update(city)
        updated_city = self.datamanager.read(city.id, City)
        self.assertEqual(updated_city.name, 'Updated City')

        # Suppression de la ville
        self.datamanager.delete(city.id, City)
        deleted_city = self.datamanager.read(city.id, City)
        self.assertIsNone(deleted_city)

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
