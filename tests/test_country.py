import unittest
from models.country import Country
from persistence.datamanager import DataManager
import os
import tempfile
import shutil

class TestCountryCRUD(unittest.TestCase):

    def setUp(self):
        # Create a temporary file to use as our database
        self.db_fd, self.db_path = tempfile.mkstemp()
        
        # Copy the countries.json to a temporary location
        self.countries_temp_path = tempfile.mktemp()
        shutil.copy('persistence/countries.json', self.countries_temp_path)
        
        self.data_manager = DataManager(self.db_path, self.countries_temp_path)
        
    def tearDown(self):
        # Close and remove the temporary database file
        os.close(self.db_fd)
        os.remove(self.db_path)
        os.remove(self.countries_temp_path)
    
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
