import unittest
import os
import json
import tempfile
import shutil
from models.country import Country
from persistence.datamanager import DataManager


class TestCountryCRUD(unittest.TestCase):

    def setUp(self):
        """
        Set up the test case.
        Create a temporary file to use as our database.
        Copy the countries.json to a temporary location.
        Initialize the DataManager object.
        """
        self.db_fd, self.db_path = tempfile.mkstemp()
        self.countries_temp_path = tempfile.mkstemp()[1]
        shutil.copy('persistence/countries.json', self.countries_temp_path)
        self.data_manager = DataManager(self.db_path, self.countries_temp_path)

    def tearDown(self):
        """
        Clean up after the test case.
        Close and remove the temporary database file.
        Remove the temporary countries.json file.
        """
        os.close(self.db_fd)
        os.remove(self.db_path)
        os.remove(self.countries_temp_path)

    def test_create_country(self):
        """
        Test case for creating a country.
        Create a new Country object.
        Call the create_country method of the DataManager object.
        Retrieve the country from the database and check its attributes.
        """
        country = Country(name="Germany", code="DE")
        self.data_manager.create_country(country)
        retrieved_country = self.data_manager.read_country(country.code)
        self.assertIsNotNone(retrieved_country)
        self.assertEqual(retrieved_country.name, "Germany")
        self.assertEqual(retrieved_country.code, "DE")

    def test_read_country(self):
        """
        Test case for reading a country.
        Create a new Country object.
        Call the create_country method of the DataManager object.
        Retrieve the country from the database and check its attributes.
        """
        country = Country(name="Germany", code="DE")
        self.data_manager.create_country(country)
        retrieved_country = self.data_manager.read_country(country.code)
        self.assertIsNotNone(retrieved_country)
        self.assertEqual(retrieved_country.name, "Germany")

    def test_update_country(self):
        """
        Test case for updating a country.
        Create a new Country object.
        Call the create_country method of the DataManager object.
        Update the country's name attribute.
        Call the update_country method of the DataManager object.
        Retrieve the country from the database and check its updated name.
        """
        country = Country(name="Germany", code="DE")
        self.data_manager.create_country(country)
        country.name = "Deutschland"
        self.data_manager.update_country(country)
        retrieved_country = self.data_manager.read_country(country.code)
        self.assertEqual(retrieved_country.name, "Deutschland")

    def test_delete_country(self):
        """
        Test case for deleting a country.
        Create a new Country object.
        Call the create_country method of the DataManager object.
        Call the delete_country method of the DataManager object.
        Retrieve the country from the database and check that it is None.
        """
        country = Country(name="Germany", code="DE")
        self.data_manager.create_country(country)
        self.data_manager.delete_country(country.code)
        retrieved_country = self.data_manager.read_country(country.code)
        self.assertIsNone(retrieved_country)


if __name__ == "__main__":
    unittest.main()
