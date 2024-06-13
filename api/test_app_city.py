import unittest
import json
from api.app_city import app  # Assurez-vous d'importer correctement votre application Flask ou Blueprint des villes

class TestCityEndpoints(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.headers = {'Content-Type': 'application/json'}

    def tearDown(self):
        # Clean up any data after each test if needed
        pass

    def test_create_city(self):
        data = {
            'name': 'Test City',
            'country_code': 'US'
        }
        response = self.app.post('/cities', headers=self.headers, data=json.dumps(data))
        self.assertEqual(response.status_code, 201)
        city_data = json.loads(response.data)
        self.assertEqual(city_data['name'], data['name'])
        self.assertEqual(city_data['country_code'], data['country_code'])

    def test_get_all_cities(self):
        response = self.app.get('/cities', headers=self.headers)
        self.assertEqual(response.status_code, 200)
        cities_data = json.loads(response.data)
        self.assertTrue(isinstance(cities_data, list))
        # Add more assertions as needed based on your API response structure

    def test_get_city(self):
        # Create a test city first
        test_city_data = {
            'name': 'Test City',
            'country_code': 'US'
        }
        response = self.app.post('/cities', headers=self.headers, data=json.dumps(test_city_data))
        self.assertEqual(response.status_code, 201)
        city_data = json.loads(response.data)
        city_id = city_data['id']

        response = self.app.get(f'/cities/{city_id}', headers=self.headers)
        self.assertEqual(response.status_code, 200)
        fetched_city_data = json.loads(response.data)
        self.assertEqual(fetched_city_data['name'], test_city_data['name'])
        self.assertEqual(fetched_city_data['country_code'], test_city_data['country_code'])

    def test_update_city(self):
        # Create a test city first
        test_city_data = {
            'name': 'Test City',
            'country_code': 'US'
        }
        response = self.app.post('/cities', headers=self.headers, data=json.dumps(test_city_data))
        self.assertEqual(response.status_code, 201)
        city_data = json.loads(response.data)
        city_id = city_data['id']

        updated_data = {
            'name': 'Updated City Name',
            'country_code': 'FR'
        }
        response = self.app.put(f'/cities/{city_id}', headers=self.headers, data=json.dumps(updated_data))
        self.assertEqual(response.status_code, 200)
        updated_city_data = json.loads(response.data)
        self.assertEqual(updated_city_data['name'], updated_data['name'])
        self.assertEqual(updated_city_data['country_code'], updated_data['country_code'])

    def test_delete_city(self):
        # Create a test city first
        test_city_data = {
            'name': 'Test City',
            'country_code': 'US'
        }
        response = self.app.post('/cities', headers=self.headers, data=json.dumps(test_city_data))
        self.assertEqual(response.status_code, 201)
        city_data = json.loads(response.data)
        city_id = city_data['id']

        response = self.app.delete(f'/cities/{city_id}', headers=self.headers)
        # Verify the city is deleted or not found in subsequent request

if __name__ == '__main__':
    unittest.main()

