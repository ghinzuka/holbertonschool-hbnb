import unittest
import json
from api.app_amenity import app, amenity_data_manager
from models.amenity import Amenities

class TestAmenityAPI(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        # Clear amenity_data_manager data for a clean test environment
        amenity_data_manager.data = {}
        amenity_data_manager.save_data()

    def test_create_amenity(self):
        amenity_data = {
            'name': 'WiFi'
        }
        response = self.app.post('/amenities/', data=json.dumps(amenity_data), content_type='application/json')
        print(f"Create Amenity Response: {response.json}")
        self.assertEqual(response.status_code, 201)
        self.assertIn('id', response.json)
        self.created_amenity_id = response.json['id']

    def test_get_amenity(self):
        # Create an amenity to test
        amenity_data = {
            'name': 'Pool'
        }
        create_response = self.app.post('/amenities/', data=json.dumps(amenity_data), content_type='application/json')
        amenity_id = create_response.json['id']
        
        response = self.app.get(f'/amenities/{amenity_id}')
        print(f"Get Amenity Response: {response.json}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['name'], amenity_data['name'])

    def test_update_amenity(self):
        # Create an amenity to test
        amenity_data = {
            'name': 'Gym'
        }
        create_response = self.app.post('/amenities/', data=json.dumps(amenity_data), content_type='application/json')
        amenity_id = create_response.json['id']
        
        updated_amenity_data = {
            'name': 'Fitness Center'
        }
        response = self.app.put(f'/amenities/{amenity_id}', data=json.dumps(updated_amenity_data), content_type='application/json')
        print(f"Update Amenity Response: {response.json}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['name'], updated_amenity_data['name'])

    def test_delete_amenity(self):
        # Create an amenity to test
        amenity_data = {
            'name': 'Sauna'
        }
        create_response = self.app.post('/amenities/', data=json.dumps(amenity_data), content_type='application/json')
        amenity_id = create_response.json['id']
        
        response = self.app.delete(f'/amenities/{amenity_id}')
        print(f"Delete Amenity Response Status Code: {response.status_code}")
        self.assertEqual(response.status_code, 204)
        
        # Verify amenity is deleted
        response = self.app.get(f'/amenities/{amenity_id}')
        print(f"Get Deleted Amenity Response: {response.json}")
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
