import unittest
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from persistence.datamanager import DataManager
from models.city import City

class TestCity(unittest.TestCase):
    def setUp(self):
        # Créer une instance de DataManager avec un chemin de fichier spécifique pour le stockage des données JSON
        self.file_path = "test_cities.json"  # Chemin de fichier pour stocker les données JSON
        self.datamanager = DataManager(self.file_path)

    def tearDown(self):
        # Supprimer le fichier JSON après chaque test
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_city_crud(self):
        # Création d'une ville
        city = City(name='New York')
        self.datamanager.create(city)

        # Récupération de la ville
        retrieved_city = self.datamanager.read(city.id, City)
        self.assertEqual(retrieved_city.name, 'New York')
        self.assertIsNotNone(retrieved_city.id)  # Vérifier que l'ID a été correctement défini

        # Mise à jour de la ville
        city.name = 'San Francisco'
        self.datamanager.update(city)
        updated_city = self.datamanager.read(city.id, City)
        self.assertEqual(updated_city.name, 'San Francisco')

        # Suppression de la ville
        self.datamanager.delete(city.id, City)
        deleted_city = self.datamanager.read(city.id, City)
        self.assertIsNone(deleted_city)

if __name__ == '__main__':
    unittest.main()
