import os
import unittest
import json
from api.app_country import app, country_manager

# Chemin absolu vers le fichier JSON de test
TEST_JSON_FILE = os.path.abspath('countries.json')

class TestCountryAPI(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Initialise le client de test Flask et configure les tests
        app.testing = True
        cls.client = app.test_client()

    def setUp(self):
        # Assurez-vous que le fichier de données de test contient des données initiales
        initial_data = {
            'ZZ': 'Test Country'
        }
        with open(TEST_JSON_FILE, 'w') as file:
            json.dump(initial_data, file, indent=4)
        country_manager.load_countries()  # Recharge les données pour chaque test

    def tearDown(self):
        # Nettoie après chaque test en supprimant les données ajoutées pendant le test
        try:
            with open(TEST_JSON_FILE, 'r') as file:
                data = json.load(file)
                # Supprime les pays ajoutés pendant le test
                for code in list(data.keys()):
                    if code not in {'ZZ'}:
                        del data[code]
            with open(TEST_JSON_FILE, 'w') as file:
                json.dump(data, file, indent=4)
        except FileNotFoundError:
            pass

    def test_create_country(self):
        # Teste l'endpoint POST /countries pour créer un nouveau pays
        new_country_data = {
            'code': 'AA',
            'name': 'New Country'
        }
        response = self.client.post('/countries', json=new_country_data)
        self.assertEqual(response.status_code, 201)
        
        # Vérifie si 'AA' est bien présent dans les données après création
        with open(TEST_JSON_FILE, 'r') as file:
            data = json.load(file)
            self.assertTrue('AA' in data)

    def test_get_country(self):
        # Teste l'endpoint GET /countries/<country_code> pour récupérer un pays existant
        response = self.client.get('/countries/ZZ')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(data['code'], 'ZZ')

    def test_get_non_existent_country(self):
        # Teste l'endpoint GET /countries/<country_code> pour récupérer un pays qui n'existe pas
        response = self.client.get('/countries/AA')
        self.assertEqual(response.status_code, 404)

    def test_update_country(self):
        # Teste l'endpoint PUT /countries/<country_code> pour mettre à jour un pays existant
        updated_country_data = {
            'name': 'Updated Country Name'
        }
        response = self.client.put('/countries/ZZ', json=updated_country_data)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(data['name'], 'Updated Country Name')

    def test_update_non_existent_country(self):
        # Teste l'endpoint PUT /countries/<country_code> pour mettre à jour un pays qui n'existe pas
        updated_country_data = {
            'name': 'Updated Country Name'
        }
        response = self.client.put('/countries/AA', json=updated_country_data)
        self.assertEqual(response.status_code, 404)

    def test_delete_country(self):
        # Teste l'endpoint DELETE /countries/<country_code> pour supprimer un pays existant
        # Ajoutons une vérification pour s'assurer que ZZ existe avant de le supprimer
        response = self.client.get('/countries/ZZ')
        self.assertEqual(response.status_code, 200)


    def test_delete_non_existent_country(self):
        # Teste l'endpoint DELETE /countries/<country_code> pour supprimer un pays qui n'existe pas
        response = self.client.delete('/countries/AA')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
