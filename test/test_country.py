import unittest
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from persistence.datamanager import DataManager
from models.country import Country
from models.city import City

class TestCountry(unittest.TestCase):
    def setUp(self):
        # Créer une instance de DataManager avec un chemin de fichier spécifique pour le stockage des données JSON
        self.file_path = "test_countries.json"  # Chemin de fichier pour stocker les données JSON
        self.datamanager = DataManager(self.file_path)

    def tearDown(self):
        # Supprimer le fichier JSON après chaque test
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_country_crud(self):
        # Création d'une ville
        city = City(name='Paris')
        self.datamanager.create(city)

        # Création d'un pays
        country = Country(city=city, name='France')
        self.datamanager.create(country)

        # Récupération du pays
        retrieved_country = self.datamanager.read(country.id, Country)
        self.assertEqual(retrieved_country.name, 'France')
        self.assertEqual(retrieved_country.city.name, 'Paris')

        # Mise à jour du pays
        country.name = 'Germany'
        self.datamanager.update(country)
        updated_country = self.datamanager.read(country.id, Country)
        self.assertEqual(updated_country.name, 'Germany')

        # Suppression du pays
        self.datamanager.delete(country.id, Country)
        deleted_country = self.datamanager.read(country.id, Country)
        self.assertIsNone(deleted_country)

if __name__ == '__main__':
    unittest.main()
