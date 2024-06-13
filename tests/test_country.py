import unittest
import json
import os
from models.country import Country
from persistence.country_manager import CountryManager  # Assurez-vous que le chemin d'importation est correct

# Définir un chemin temporaire pour les tests
TEST_COUNTRIES_FILE = 'test_countries.json'

class TestCountryManager(unittest.TestCase):
    def setUp(self):
        # Créer un gestionnaire de pays pour les tests avec un fichier temporaire
        self.manager = CountryManager(TEST_COUNTRIES_FILE)

    def tearDown(self):
        # Supprimer le fichier temporaire après chaque test
        if os.path.exists(TEST_COUNTRIES_FILE):
            os.remove(TEST_COUNTRIES_FILE)

    def test_create_country(self):
        country = Country('US', 'United States')
        self.manager.create_country(country)

        # Vérifier si le pays a été correctement ajouté
        self.assertTrue(self.manager.is_valid_country_code('US'))

    def test_read_country(self):
        country = Country('CA', 'Canada')
        self.manager.create_country(country)

        # Lire le pays ajouté et vérifier s'il est correct
        retrieved_country = self.manager.read_country('CA')
        self.assertEqual(retrieved_country.name, 'Canada')

    def test_update_country(self):
        country = Country('FR', 'France')
        self.manager.create_country(country)

        # Mettre à jour le nom du pays
        updated_country = Country('FR', 'French Republic')
        self.manager.update_country(updated_country)

        # Lire à nouveau le pays pour vérifier la mise à jour
        retrieved_country = self.manager.read_country('FR')
        self.assertEqual(retrieved_country.name, 'French Republic')

    def test_delete_country(self):
        country = Country('DE', 'Germany')
        self.manager.create_country(country)

        # Supprimer le pays ajouté
        self.manager.delete_country('DE')

        # Vérifier si le pays a été supprimé
        self.assertFalse(self.manager.is_valid_country_code('DE'))

    def test_invalid_country_code(self):
        # Vérifier un code de pays invalide
        self.assertFalse(self.manager.is_valid_country_code('ZZ'))

    def test_load_countries(self):
        # Vérifier le chargement initial des pays
        initial_countries = {'US': 'United States', 'CA': 'Canada', 'FR': 'France'}
        with open(TEST_COUNTRIES_FILE, 'w') as file:
            json.dump(initial_countries, file)

        self.manager.load_countries()

        self.assertTrue(self.manager.is_valid_country_code('US'))
        self.assertTrue(self.manager.is_valid_country_code('CA'))
        self.assertTrue(self.manager.is_valid_country_code('FR'))

if __name__ == '__main__':
    unittest.main()