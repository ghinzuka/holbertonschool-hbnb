import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from persistence.datamanager import DataManager
from models.city import City
from models.country import Country

class TestCountry(unittest.TestCase):
    def setUp(self):
        # Créer une instance de DataManager avec un stockage fictif pour les tests
        self.datamanager = DataManager(MockStorage())

    def test_country_crud(self):
        # Création d'une ville pour associer au pays
        city = City('New York')
        self.datamanager.create(city)

        # Création d'un pays
        country = Country(city, 'USA')
        self.datamanager.create(country)

        # Récupération du pays
        retrieved_country = self.datamanager.read(country.id, Country)
        self.assertEqual(retrieved_country.name, 'USA')
        self.assertEqual(retrieved_country.city, city)

        # Mise à jour du pays
        country.name = 'United States'
        self.datamanager.update(country)
        updated_country = self.datamanager.read(country.id, Country)
        self.assertEqual(updated_country.name, 'United States')

        # Suppression du pays
        self.datamanager.delete(country.id, Country)
        deleted_country = self.datamanager.read(country.id, Country)
        self.assertIsNone(deleted_country)

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