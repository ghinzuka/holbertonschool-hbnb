import unittest
from app import app, users  # Assurez-vous que `app` est importé correctement depuis votre fichier principal

class UserApiTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def tearDown(self):
        users.clear()  # Réinitialise la liste des utilisateurs après chaque test

    def test_create_user(self):
        user_data = {
            'email': 'test@example.com',
            'first_name': 'Test',
            'last_name': 'User'
        }
        response = self.app.post('/users/', json=user_data)
        self.assertEqual(response.status_code, 201)
        self.assertIn('email', response.json)
        self.assertIn('first_name', response.json)
        self.assertIn('last_name', response.json)
        self.assertIn('id', response.json)
        self.assertIn('created_at', response.json)
        self.assertIn('updated_at', response.json)

    def test_create_user_invalid_email(self):
        user_data = {
            'email': 'invalid-email',
            'first_name': 'Test',
            'last_name': 'User'
        }
        response = self.app.post('/users/', json=user_data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json['message'], 'Invalid email format')

    def test_create_user_duplicate_email(self):
        user_data = {
            'email': 'test@example.com',
            'first_name': 'Test',
            'last_name': 'User'
        }
        self.app.post('/users/', json=user_data)
        response = self.app.post('/users/', json=user_data)
        self.assertEqual(response.status_code, 409)
        self.assertEqual(response.json['message'], 'Email already exists')

if __name__ == '__main__':
    unittest.main()
