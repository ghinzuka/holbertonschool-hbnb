import unittest
import os
import json
import tempfile
import shutil
from models.country import Country
from persistence.datamanager import DataManager

class TestCountryCRUD(unittest.TestCase):

    def setUp(self):
        # Créer un fichier temporaire pour la base de données
        self.db_fd, self.db_path = tempfile.mkstemp(suffix='.json')
        
        # Chemin vers countries.json dans le dossier persistence/
        countries_json_path = os.path.join(os.path.dirname(__file__), '..', 'persistence', 'countries.json')
        
        # Créer une instance de DataManager avec les chemins appropriés
        self.data_manager = DataManager(file_path=self.db_path,
                                        countries_file_path=countries_json_path)
        
    def tearDown(self):
        # Fermer et supprimer le fichier de base de données temporaire
        os.close(self.db_fd)
        os.remove(self.db_path)

    def test_create_country(self):
        country = Country(name="Germany", code="DE")
        self.data_manager.create_country(country)
        retrieved_country = self.data_manager.read_country(country.code)
        self.assertIsNotNone(retrieved_country)
        self.assertEqual(retrieved_country.name, "Germany")
        self.assertEqual(retrieved_country.code, "DE")
    
    def test_read_country(self):
        country = Country(name="Germany", code="DE")
        self.data_manager.create_country(country)
        retrieved_country = self.data_manager.read_country(country.code)
        self.assertIsNotNone(retrieved_country)
        self.assertEqual(retrieved_country.name, "Germany")
    
    def test_update_country(self):
        country = Country(name="Germany", code="DE")
        self.data_manager.create_country(country)
        country.name = "Deutschland"
        self.data_manager.update_country(country)
        retrieved_country = self.data_manager.read_country(country.code)
        self.assertEqual(retrieved_country.name, "Deutschland")
    
    def test_delete_country(self):
        country = Country(name="Germany", code="DE")
        self.data_manager.create_country(country)
        self.data_manager.delete_country(country.code)
        retrieved_country = self.data_manager.read_country(country.code)
        self.assertIsNone(retrieved_country)

if __name__ == "__main__":
    unittest.main()
