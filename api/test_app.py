from flask_testing import TestCase
from flask import url_for
from api.app import app
from persistence.datamanager import DataManager
from models.user import User

class TestUserAPI(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        return app

    def setUp(self):
        # Préparer l'environnement pour chaque test
        self.data_manager = DataManager('test_data.json')
        self.data_manager.data = {}  # Réinitialiser les données pour chaque test

    def tearDown(self):
        # Nettoyer l'environnement après chaque test
        self.data_manager.data = {}

    def test_list_users(self):
        response = self.client.get(url_for('users_user_list'))
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)

    def test_create_user(self):
        response = self.client.post(url_for('users_user_list'), json={
            'email': 'test@example.com',
            'password': 'password123',
            'first_name': 'Test',
            'last_name': 'User'
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn('email', response.json)
        self.assertEqual(response.json['email'], 'test@example.com')


if __name__ == '__main__':
    import unittest
    unittest.main()