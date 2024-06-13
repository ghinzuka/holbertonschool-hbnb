import unittest
import json
from api.app_city import app  # Assurez-vous d'importer correctement votre application Flask ou Blueprint des villes
from models.city import City
from persistence.datamanager import DataManager

class TestCityAPI(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

        # Créer une nouvelle instance de DataManager pour chaque test
        self.data_manager = DataManager('city_data.json', 'persistence/countries.json')

        # Peupler city_data.json avec des données de test
        self.populate_city_data()

    def populate_city_data(self):
        # Créer quelques villes de test
        paris = City(name='Paris', country_code='FR')
        london = City(name='London', country_code='GB')
        berlin = City(name='Berlin', country_code='DE')

        # Ajouter les villes à DataManager en utilisant self.data_manager
        self.data_manager.create_city(paris)
        self.data_manager.create_city(london)
        self.data_manager.create_city(berlin)

        # Imprimer les IDs des villes peuplées
        print(f"IDs des villes peuplées : {paris.id}, {london.id}, {berlin.id}")

    def test_list_cities(self):
        response = self.app.get('/cities/')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data.decode('utf-8'))
        self.assertTrue(isinstance(data, list))
        self.assertGreater(len(data), 0)  # Vérifie qu'il y a au moins une ville dans la liste

    def test_create_city(self):
        new_city_data = {'name': 'New City', 'country_code': 'US'}
        response = self.app.post('/cities/', json=new_city_data)
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(data['name'], new_city_data['name'])
        self.assertEqual(data['country_code'], new_city_data['country_code'])

    def test_get_city(self):
        response = self.app.get('/cities/1')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(data['name'], 'Paris')  # Assurez-vous que l'ID 1 correspond à Paris

    def test_update_city(self):
        updated_city_data = {'name': 'Updated City'}
        response = self.app.put('/cities/1', json=updated_city_data)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(data['name'], updated_city_data['name'])

    def test_delete_city(self):
        response = self.app.delete('/cities/1')
        self.assertEqual(response.status_code, 204)

if __name__ == '__main__':
    unittest.main()
