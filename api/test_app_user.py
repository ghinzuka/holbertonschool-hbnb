import unittest
import json
from api.app_user import app, data_manager
from models.user import User

class TestUserAPI(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        data_manager.data = {}
        data_manager.save_data()

    def test_create_user(self):
        user_data = {
            'email': 'testuser@example.com',
            'password': 'password123',
            'first_name': 'Test',
            'last_name': 'User'
        }
        response = self.app.post('/users/', data=json.dumps(user_data), content_type='application/json')
        print(f"Create User Response: {response.json}")
        self.assertEqual(response.status_code, 201)
        self.assertIn('id', response.json)
        self.created_user_id = response.json['id']

    def test_get_user(self):
        user_data = {
            'email': 'fetchuser@example.com',
            'password': 'password123',
            'first_name': 'Fetch',
            'last_name': 'User'
        }
        create_response = self.app.post('/users/', data=json.dumps(user_data), content_type='application/json')
        user_id = create_response.json['id']
        
        response = self.app.get(f'/users/{user_id}')
        print(f"Get User Response: {response.json}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['email'], user_data['email'])

    def test_update_user(self):
        user_data = {
            'email': 'updateuser@example.com',
            'password': 'password123',
            'first_name': 'Update',
            'last_name': 'User'
        }
        create_response = self.app.post('/users/', data=json.dumps(user_data), content_type='application/json')
        user_id = create_response.json['id']
        
        updated_user_data = {
            'email': 'updateduser@example.com',
            'password': 'newpassword123',
            'first_name': 'Updated',
            'last_name': 'User'
        }
        response = self.app.put(f'/users/{user_id}', data=json.dumps(updated_user_data), content_type='application/json')
        print(f"Update User Response: {response.json}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['email'], updated_user_data['email'])

    def test_delete_user(self):
        user_data = {
            'email': 'deleteuser@example.com',
            'password': 'password123',
            'first_name': 'Delete',
            'last_name': 'User'
        }
        create_response = self.app.post('/users/', data=json.dumps(user_data), content_type='application/json')
        user_id = create_response.json['id']
        
        response = self.app.delete(f'/users/{user_id}')
        print(f"Delete User Response Status Code: {response.status_code}")
        self.assertEqual(response.status_code, 204)
        
        response = self.app.get(f'/users/{user_id}')
        print(f"Get Deleted User Response: {response.json}")
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()